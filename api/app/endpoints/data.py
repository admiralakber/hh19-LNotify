from faker import Faker
from collections import OrderedDict
import random

fake = Faker()

doctors = [("Dr Mark Butterworth", "The Prince Charles Hospital (TPCH) - Rode Road CHERMSIDE QLD 4032 Phone: (07) 3139 4000"),
("Dr Robert Stable", "The Prince Charles Hospital (TPCH) -  Rode Road CHERMSIDE QLD 4032, Phone: (07) 3139 4000"),
("Dr Clair Sullivan", "Redcliffe Hospital (RED) - Anzac Avenue REDCLIFFE QLD 4020 Phone: (07) 3883 7777"),
("Dr Vicki Columbus", "Caboolture Hospital CAB - McKean Street CABOOLTURE QLD 4510 Phone: (07) 5433 8888"),
("Dr Rebecca He", "Kilcoy Hospital (KIL) - 12 Kropp Street KILCOY QLD 4515 Phone: (07) 5422 4411"),
("Dr Leonnie Anderson", "The Prince Charles Hospital (TPCH) - Rode Road CHERMSIDE QLD 4032 Phone: (07) 3139 4000"),
("Dr Liz Rushbrook", "Redcliffe Hospital (RED) - Anzac Avenue REDCLIFFE QLD 4020 Phone: (07) 3883 7777"),
("Dr Elizabeth Whiting", "Caboolture Hospital CAB - McKean Street CABOOLTURE QLD 4510 Phone: (07) 5433 8888"),
("Dr Jason Jenkins", "Kilcoy Hospital (KIL) - 12 Kropp Street KILCOY QLD 4515 Phone: (07) 5422 4411"),
("Dr Lance Le Ray", "The Prince Charles Hospital (TPCH) - Rode Road CHERMSIDE QLD 4032 Phone: (07) 3139 4000")]

patients = OrderedDict({})

patient = { "id" : "0", 
            "name" : "Swee Teng",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "mandarin",
                    "preferred" : True
                },
                {
                    "language" : "cantonese",
                    "preferred" : False
                }
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient

patient = { "id" : "1", 
            "name" : "Krishna Prasad",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "Hindi",
                    "preferred" : True
                },
                {
                    "language" : "Punjabi",
                    "preferred" : False
                }
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient

patient = { "id" : "2", 
            "name" : "Hamelmal Gebru ",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "Amharic",
                    "preferred" : True
                }
        
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient

patient = { "id" : "3", 
            "name" : "Olga Zbarskaya",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "Russia",
                    "preferred" : True
                }
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient

patient = { "id" : "4", 
            "name" : "Aye Aye Kyaw",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "Burmese",
                    "preferred" : True
                },
                {
                    "language" : "Karen",
                    "preferred" : False
                }
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient

patient = { "id" : "5", 
            "name" : "Mafada Abduallah",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "Persian Farsi",
                    "preferred" : True
                }
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient

patient = { "id" : "6", 
            "name" : "Pham Le",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "Vietnamese",
                    "preferred" : True
                }
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient

patient = { "id" : "7", 
            "name" : "Alfonsi Bellucci",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "Italian",
                    "preferred" : True
                }
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient

patient = { "id" : "8", 
            "name" : "Ahmed Abduallah",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "Arabic",
                    "preferred" : True
                }
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient

patient = { "id" : "9", 
            "name" : "Milivoje Tomasevic",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "Bosnian",
                    "preferred" : True
                }
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient

patient = { "id" : "10", 
            "name" : "Va’a Alofipo’s",
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "Samoan",
                    "preferred" : True
                }
            ],
            "generalPractitioner" : random.choice(doctors)[0],
            "managingOrganization" : random.choice(doctors)[1]
}
patients[patient["id"]] = patient