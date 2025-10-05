from load_data import load_data
from clean_data import clean_data
from evaluate import WaterQualityEvaluator

def main():
    # Step 1: Load Data
    df = load_data("data/sensor_data.csv")
    if df.empty:
        print("⚠️ No data to process.")
        return

    # Step 2: Clean Data
    df = clean_data(df)

    # Step 3: Evaluate Water Quality
    evaluator = WaterQualityEvaluator()

    print("\n💧 WATER QUALITY REPORT\n" + "-" * 30)
    for _, row in df.iterrows():
        safe, reason = evaluator.is_safe(row['ph'], row['turbidity'])
        status = "✅ Safe" if safe else f"❌ Unsafe ({reason})"
        print(f"Sensor {row['sensor_id']} at {row['location']}: {status}")

if __name__ == "__main__":
    main()
