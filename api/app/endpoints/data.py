from faker import Faker
from collections import OrderedDict

fake = Faker()

doctors = [("Dr {}".format(fake.name()), "RBWH, Maternity"), 
            ("Dr {}".format(fake.name()), "RBWH, Maternity"), 
            ("Dr {}".format(fake.name()), "RBWHM Maternity")]

patients = OrderedDict({})

# arabic, egypt
patient = { "id" : "0", 
            "name" : fake.name(),
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "arabic",
                    "preferred" : True
                }
            ],
            "generalPractitioner" : doctors[0][0],
            "managingOrganization" : doctors[0][1]
}
patients[patient["id"]] = patient

# chinese
patient = { "id" : "1", 
            "name" : fake.name(),
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "chinese",
                    "preferred" : True
                }
            ],
            "generalPractitioner" : doctors[1][0],
            "managingOrganization" : doctors[1][1]
}
patients[patient["id"]] = patient

# urdu
patient = { "id" : "2", 
            "name" : fake.name(),
            "telecom" : [
                {
                    "system" : "phone",
                    "value" : "0430204771"
                }
            ],
            "communication" : [
                {
                    "language" : "urdu",
                    "preferred" : True
                }
            ],
            "generalPractitioner" : doctors[2][0],
            "managingOrganization" : doctors[2][1]
}
patients[patient["id"]] = patient

