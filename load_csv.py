import pandas as pd
import sys

def load(path: str) -> pd.DataFrame:
    """Loads a CSV file into a pandas DataFrame, prints its dimensions,

    and handles error exceptions.
    """
    try:
        # 1. Cargar el dataset usando pandas
        df = pd.read_csv(path)
        
        # 2. Imprimir las dimensiones usando la propiedad .shape (devuelve (filas, columnas))
        print(f"Loading dataset of dimensions {df.shape}")
        
        # 3. Retornar el dataset (DataFrame)
        return df

    except FileNotFoundError:
        print(f"Error: El archivo en la ruta '{path}' no existe.", file=sys.stderr)
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo '{path}' está vacío.", file=sys.stderr)
        return None
    except pd.errors.ParserError:
        print(f"Error: El archivo '{path}' no tiene un formato CSV válido.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error inesperado: {e}", file=sys.stderr)
        return None