import yaml

with open("example.yml", "r") as yamlData:
    data = yaml.load(yamlData,Loader=yaml.CLoader) #yaml.CLoader：輕量級的解析器，比較快
                                                   #yaml.FullLoader:完整解析器，比較靈活比較慢
    print(data)

    for d in data:
        print(d)
        print(data[d])
