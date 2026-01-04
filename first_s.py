import pandas as pd
import numpy as np

def load_cloud_ddos_data(filepath):
    """
    Load BCCC-cPacket-Cloud-DDoS-2024 dataset from parquet file
    
    Args:
        filepath: Path to parquet file
        
    Returns:
        DataFrame with network traffic
    """
    print(f"Loading BCCC-Cloud-DDoS-2024 dataset...")
    print(f"File: {filepath}")
    print("-" * 50)
    
    # Load parquet file
    df = pd.read_parquet(filepath)
    
    # Basic info
    print(f"\n✓ Successfully loaded {len(df):,} records")
    print(f"✓ Features: {len(df.columns)} columns")
    print(f"✓ Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    print(f"\nLabel distribution:")
    label_counts = df['Label'].value_counts()
    for label, count in label_counts.items():
        print(f"  {label}: {count:,}")
    
    print(f"\nDataset shape: {df.shape}")
    print("-" * 50)
    
    return df

if __name__ == "__main__":
    # Test the loader
    data_path = "../data/your_file.parquet"  # Update with actual filename
    
    df = load_cloud_ddos_data(data_path)
    
    print(f"\nFirst 5 rows:")
    print(df.head())
