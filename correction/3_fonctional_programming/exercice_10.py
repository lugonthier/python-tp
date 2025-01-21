from abc import ABC, abstractmethod
from functools import wraps
import time
import logging
from typing import Any, Callable
import tracemalloc
from datetime import datetime, timedelta
from collections import deque

logging.basicConfig(level=logging.INFO)

def retry(max_attempts: int = 3, delay: float = 1.0):
    """Réessaie une fonction en cas d'échec."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logging.warning(f"Tentative {attempt + 1}/{max_attempts} échouée: {str(e)}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

def rate_limit(calls: int, period: int):
    """Limite le nombre d'appels à une fonction sur une période donnée."""
    def decorator(func: Callable) -> Callable:
        history = deque(maxlen=calls)
        
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            now = datetime.now()
            while history and (now - history[0]) > timedelta(seconds=period):
                history.popleft()
                
            if len(history) >= calls:
                raise Exception(f"Rate limit dépassé: {calls} appels/{period}s")
                
            history.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_args(*types, **bounds):
    """Valide les types et les bornes des arguments."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for arg, expected_type in zip(args[1:], types):  # Skip self
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {arg} doit être de type {expected_type}")
            
            for arg_name, (min_val, max_val) in bounds.items():
                if arg_name in kwargs:
                    val = kwargs[arg_name]
                    if val < min_val or val > max_val:
                        raise ValueError(
                            f"{arg_name} doit être entre {min_val} et {max_val}"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def measure_performance(func: Callable) -> Callable:
    """Mesure le temps d'exécution et la consommation mémoire."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        tracemalloc.start()
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        logging.info(f"{func.__name__}:"
                    f" Temps: {end_time - start_time:.4f}s,"
                    f" Mémoire actuelle: {current / 1024:.2f}KB,"
                    f" Pic mémoire: {peak / 1024:.2f}KB")
        return result
    return wrapper

class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int, **kwargs):
        self.brand = brand
        self.model = model
        self.year = year
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @abstractmethod
    @measure_performance
    def calculate_cost_per_km(self) -> float:
        """Calcule le coût par kilomètre."""
        pass
    
    @retry(max_attempts=3)
    def fetch_current_energy_price(self) -> float:
        """Simule un appel API pour obtenir le prix de l'énergie."""
        import random
        if random.random() < 0.5:
            raise ConnectionError("Erreur de connexion à l'API")
        return random.uniform(1.5, 2.5)

class Car(Vehicle):
    def __init__(self, fuel_capacity: float, fuel_consumption: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption
    
    @validate_args(float, fuel_price=(0, float('inf')))
    @measure_performance
    def calculate_cost_per_km(self, fuel_price: float = None) -> float:
        if fuel_price is None:
            fuel_price = self.fetch_current_energy_price()
        return self.fuel_consumption * fuel_price / 100  # L/100km → €/km

class ElectricCar(Vehicle):
    def __init__(self, battery_capacity: float, energy_consumption: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.battery_capacity = battery_capacity
        self.energy_consumption = energy_consumption
    
    @validate_args(float, electricity_price=(0, float('inf')))
    @measure_performance
    @rate_limit(calls=100, period=60)
    def calculate_cost_per_km(self, electricity_price: float = None) -> float:
        if electricity_price is None:
            electricity_price = self.fetch_current_energy_price()
        return self.energy_consumption * electricity_price / 100  # kWh/100km → €/km

class HybridCar(Car, ElectricCar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @measure_performance
    def calculate_cost_per_km(self, fuel_price: float = None, electricity_price: float = None) -> float:
        thermal_cost = super(Car, self).calculate_cost_per_km(fuel_price)
        electric_cost = super(ElectricCar, self).calculate_cost_per_km(electricity_price)
        return (thermal_cost + electric_cost) / 2

if __name__ == "__main__":
    car = Car(
        brand="Toyota",
        model="Corolla",
        year=2020,
        fuel_capacity=50,
        fuel_consumption=5.5,
        color="red" 
    )

    electric_car = ElectricCar(
        brand="Tesla",
        model="Model 3",
        year=2022,
        battery_capacity=75,
        energy_consumption=16,
        autopilot_version="3.0"  
    )

    hybrid_car = HybridCar(
        brand="Toyota",
        model="Prius",
        year=2023,
        fuel_capacity=43,
        fuel_consumption=4.5,
        battery_capacity=8.8,
        energy_consumption=10,
        driving_modes=["ECO", "POWER", "NORMAL"]
    )

    try:
        print(f"\nCoût au km (thermique): {car.calculate_cost_per_km():.2f}€")
        print(f"Coût au km (électrique): {electric_car.calculate_cost_per_km():.2f}€")
        print(f"Coût au km (hybride): {hybrid_car.calculate_cost_per_km():.2f}€")
    except Exception as e:
        print(f"Erreur lors du calcul des coûts: {str(e)}")

    print("\nTest du rate limiting:")
    for i in range(3):
        try:
            electric_car.calculate_cost_per_km()
            print(f"Appel {i+1} réussi")
        except Exception as e:
            print(f"Appel {i+1} échoué: {str(e)}")

    print("\nAttributs des véhicules:")
    for vehicle in [car, electric_car, hybrid_car]:
        print(f"\n{vehicle.__class__.__name__}:")
        for attr, value in vehicle.__dict__.items():
            print(f"  {attr}: {value}")