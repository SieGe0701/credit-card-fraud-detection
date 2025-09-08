import subprocess
import sys

# Run preprocessing
print('Running preprocessing...')
preprocess_result = subprocess.run([sys.executable, 'src/preprocess.py'], capture_output=True, text=True)
print(preprocess_result.stdout)
if preprocess_result.returncode != 0:
    print('Preprocessing failed:', preprocess_result.stderr)
    sys.exit(1)

# Run model training
print('Running model training...')
train_result = subprocess.run([sys.executable, 'src/train_model.py'], capture_output=True, text=True)
print(train_result.stdout)
if train_result.returncode != 0:
    print('Model training failed:', train_result.stderr)
    sys.exit(1)

print('Automation complete!')

# Run Flask API
print('Starting Flask API...')
api_result = subprocess.Popen([sys.executable, 'src/app.py'])
print('Flask API is running. Access it at http://127.0.0.1:5000/')
