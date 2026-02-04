#!/usr/bin/env python3
"""
Generate a large test file for processing.
Creates 5 million lines of sample data.
"""

import sys
import random
from datetime import datetime, timedelta


def generate_sample_data(num_lines=5_000_000):
    """Generate sample log data with timestamps."""
    print(f"Generating {num_lines:,} lines of sample data...")

    # Sample data patterns
    log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
    services = ['web-server', 'database', 'auth-service', 'cache', 'api-gateway']
    messages = [
        'User login successful',
        'Database query executed',
        'Cache miss occurred',
        'Request processed',
        'Connection established',
        'File uploaded',
        'Data synchronized',
        'Backup completed',
        'Error in processing',
        'Timeout occurred'
    ]

    start_time = datetime.now() - timedelta(days=30)

    with open('large_data.txt', 'w', encoding='utf-8') as f:
        for i in range(num_lines):
            if i % 100000 == 0:
                print(f"  Generated {i:,} lines...")

            # Create a timestamp
            timestamp = start_time + timedelta(seconds=i)
            timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')

            # Random components
            level = random.choice(log_levels)
            service = random.choice(services)
            message = random.choice(messages)
            user_id = random.randint(1000, 9999)
            duration = random.uniform(0.1, 5.0)

            # Create log line
            log_line = f"{timestamp_str} [{level}] {service}: {message} (user_id={user_id}, duration={duration:.3f}s)\n"
            f.write(log_line)

    print(f"✅ File 'large_data.txt' created with {num_lines:,} lines.")
    print(f"   File size: {os.path.getsize('large_data.txt') / (1024 * 1024):.2f} MB")


if __name__ == "__main__":
    import os

    # Check if file already exists
    if os.path.exists('large_data.txt'):
        print("⚠️ Warning: 'large_data.txt' already exists!")
        response = input("Do you want to regenerate it? (y/N): ")
        if response.lower() != 'y':
            print("Exiting...")
            sys.exit(0)

    try:
        generate_sample_data()
    except KeyboardInterrupt:
        print("\n\n⚠️ Generation interrupted. Partial file may exist.")
    except Exception as e:
        print(f"❌ Error: {e}")