from fastapi import FastAPI
from connexion import DB


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# aux infos d'un restaurant à partir de son id,
@app.get("/api/info/{id}")
async def get_info_by_id(id=None):
    return DB.get_info_by_id(id)

    
# à la liste des noms de restaurants à partir du type de cuisine,
@app.get("/api/name/{type_cuisine}")
async def get_resto_by_type(type_cuisine: str):
    return DB.get_name_by_type(type_cuisine)

# au nombre d'inspection d'un restaurant à partir de son id restaurant,
@app.get("/api/inspection/{idrestaurant}")
async def get_inspection_by_idrestaurant(idrestaurant: int):
    return DB.get_nb_inspec_by_id(idrestaurant)
    
# les noms des 10 premiers restaurants d'un grade donné.
@app.get("/api/classement/{grade}")
async def get_classement_by_grade(grade: str):
    return DB.get_top_10(grade)





# http://localhost:88/api/info/50041578
# http://localhost:88/api/name/Asian
# http://localhost:88/api/inspection/40859175
# http://localhost:88/api/classement/B