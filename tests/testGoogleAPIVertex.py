import unittest
import pandas as pd
from app import generate
from MockData import create_mock_data1, convert_mock_to_dict
from iterlib import thread_map

class testGoogleAPIVertex(unittest.TestCase):
    def test_generate(self):
        path1 = "Images\\test1Front.jpg"
        path2 = "Images\\test1Back.png"
        #mock_Data = create_mock_data1()
        #mock_Data = convert_mock_to_dict(mock_Data)
        responses = generate(path1, path2)
        #for response in responses:
        #    print(response)
        #mapped_gen = thread_map(lambda x: x**2, buffer_size=100, num_workers=4)
        # Générer les données et les convertir en DataFrame pandas
        #df = pd.DataFrame(mapped_gen)

        # Convertir le DataFrame en dictionnaire
        #response_dict = df.to_dict(orient="records")

        #print("Final response dictionary:", response_dict)
        
        #assert response_dict == mock_Data, "The response does not match the expected data"

if __name__ == "__main__":
    unittest.main()