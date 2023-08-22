import yaml

data = {
        "isRun": "True",
        "MotorNumber": 5 
    }

# Save
with open('example.yml', 'w') as f:
    yaml.dump(data, f, Dumper=yaml.CDumper)
