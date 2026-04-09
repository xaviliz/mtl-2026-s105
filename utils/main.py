import numpy as np
import csv


def export_to_csv(predictions, filename="predictions.csv", time_per_prediction=0.96):
    """
    Export predictions to CSV file
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['time (s)', 'instrumental', 'voice', 'prediction'])

        for i, pred in enumerate(predictions):
            timestamp = i * time_per_prediction
            prediction = "Instrumental" if pred[0] > pred[1] else "Voice"
            writer.writerow([f"{timestamp:.2f}", pred[0], pred[1], prediction])

    print(f"✅ Exported to {filename}")


def format_predictions(predictions, sample_rate=1.0, time_per_prediction=0.96):
    """
    Format VGGish model predictions with timestamps and headers.
    
    Parameters:
    - predictions: numpy array or list of predictions (n_samples, 2)
    - sample_rate: predictions per second (default 1.0)
    - time_per_prediction: seconds per prediction window (default 0.96s for VGGish)
    """
    
    print("=" * 70)
    print(f"{'Time (s)':<12} {'Instrumental':<15} {'Voice':<15} {'Prediction'}")
    print("=" * 70)
    
    for i, pred in enumerate(predictions):
        # Calculate timestamp (assuming 0.96s windows with possible overlap)
        timestamp = i * time_per_prediction
        
        # Get probabilities
        instrumental_prob = pred[0]
        voice_prob = pred[1]
        
        # Determine prediction class
        prediction_class = "Instrumental" if instrumental_prob > voice_prob else "Voice"
        
        # Format the output
        print(f"{timestamp:<12.2f} {instrumental_prob:<15.6f} {voice_prob:<15.6f} {prediction_class}")



