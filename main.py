from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import json
from bson import json_util
from pymongo import MongoClient
import datetime
from datetime import date
import dns
from fastapi import Request


api = FastAPI()
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["access-control-allow-origin"] = "*"
    return response


client = MongoClient('mongodb://oumaima_hl:Oumaimamedias24@cluster0-shard-00-00.scaj4.mongodb.net:27017,cluster0-shard-00-01.scaj4.mongodb.net:27017,cluster0-shard-00-02.scaj4.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-wu1uy5-shard-0&authSource=admin&retryWrites=true&w=majority
')

db = client['office_des_changes']

Voyages_Pays_0 = db.Voyages_Pays_0
compte_courant = db.compte_courant
Comext_import_GU_CVS = db.Comext_import_GU_CVS
Comext_Export_GU_CVS = db.Comext_Export_GU_CVS
Comext_TOTAL_CVS_CJO = db.comext_TOTAL_CVS_CJO
Dep_Voyages_Nature_0 = db.Dep_Voyages_Nature_0
Evol_MRE_3 = db.Evol_MRE_3
Evol_MRE_PAYS = db.Evol_MRE_Pays
Evol_MRE_CVS = db.Evol_MRE_CVS
Evol_voyages_CVS = db.Evol_Voyages_CVS
Evol_Recettes_Voyages_5 = db.Evol_recettes_Voyages_5
IDE_Maroc_flux_Flux_nets_par_pays_0 = db.IDE_Maroc_Flux_Flux_nets_par_pays_0
IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_0 = db.IDE_Maroc_Flux_Flux_nets_par_secteurs_NMA_0
IDE_Maroc_Flux_Par_Nature_opération_0 = db.IDE_Maroc_Flux_Par_nature_opération_0
IDE_Maroc_Recettes_par_pays_0 = db.IDE_Maroc_Recettes_par_pays_0
IDE_Maroc_Recettes_par_secteurs_0 = db.IDE_Maroc_Recettes_par_secteurs_0
IDE_Maroc_Recettes_par_secteurs_NMA_0 = db.IDE_Maroc_Recettes_par_secteurs_NMA_0
IDE_Maroc_Stock_Par_pays = db.IDE_Maroc_Stock_Par_pays
IDE_Maroc_Stock_Par_secteurs = db.IDE_Maroc_Stock_Par_secteurs
IDM_à_etranger_Stock_Par_secteurs = db.IDM_à_etranger_Stock_Par_secteurs
IDM_a_etranger_Stock_Par_pays = db.IDM_a_etranger_Stock_Par_pays
IDM_etranger_flux_par_nat_operation = db.IDM_à_etranger_Flux_Par_nature_opération_0
IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_1 = db.IDM_a_etranger_Flux_Flux_nets_par_secteurs_NMA_1
IDM_a_Etranger_Flux_Flux_nets_par_pays_0 = db.IDM_a_etranger_Flux_Flux_nets_par_pays_0
IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0 = db.IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0
IDM_a_Etranger_Flux_Depenses_par_secteurs_1 = db.IDM_a_etranger_Flux_Depenses_par_secteurs_1
IDM_a_Etranger_Flux_Depenses_par_pays_0 = db.IDM_a_etranger_Flux_Depenses_par_pays_0
IDM_a_etranger_Flux_Flux_nets_par_pays_0 = db.IDM_a_etranger_Flux_Flux_nets_par_pays_0
Balance_Services_4 = db.Balance_Services_4
imp_services_nature_4_avant2014 = db.imp_services_nature_4_avant2014
Imp_Services_Nature_4_depuis2014 = db.Imp_Services_Nature_4_depuis2014
Exp_services_nature_4_avant2014 = db.Exp_services_nature_4_avant2014
Exp_Services_Nature_4_depuis2014 = db.Exp_Services_Nature_4_depuis2014
Offshoring_3 = db.Offshoring_3
BP_A_MBP5 = db.BP_A_MBP5
BP_A_MBP6_0 = db.BP_A_MBP6_0
BP_T_MBP5 = db.BP_T_MBP5
BP_T_MBP6_3 = db.BP_T_MBP6_3
#list the collections =>
#for coll in db.list_collection_names():
#    stocker les collections dans une list

##############################compte_courant############################

@api.get('/compte_courant')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(compte_courant.find({ "date": {"$gte": start, "$lte": end} },{ "_id": 0, "date": 1, "Solde du compte courant": 1 }));
    else:
        a = list(compte_courant.find({},{ "_id": 0, "date": 1, "Solde du compte courant": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
######################################################################################################################
 ############################Comext_import_GU_CVS####################################################################
@api.get('/Comext_import_GU_CVS')
def getComptes(start: str = '', end: str = '', type: str = ''):
    if (start and end and type):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_import_GU_CVS.aggregate([{"$match": { "$and":[ {"date": {"$gte": start_date, "$lte": end_date}, "Type ": {"$eq": type}}]}}, {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, { "$project": {"_id": 0, "date": "$Date", "Type": "$Type ","Valeur": "$Valeur "}}])
    elif (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_import_GU_CVS.aggregate([{"$match": {"date": {"$gte": start_date, "$lte": end_date}}}, {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, { "$project": {"_id": 0, "date": "$Date", "Type": "$Type ","Valeur": "$Valeur "}}])
    elif (type):
          b = Comext_import_GU_CVS.aggregate([{"$match": {"Type ": {"$eq": type}}}, {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, { "$project": {"_id": 0, "date": "$Date", "Type": "$Type ","Valeur": "$Valeur "}}])
    else:
        b = Comext_import_GU_CVS.aggregate([{"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}},{"$project": {"_id": 0, "date": "$Date", "Type": "$Type ", "Valeur": "$Valeur "}}])
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(b)))
 ####################################################################################################################

####################################################################################################################
#######################################Comext_export_GU_CVS-CJO######################################################
# url ==> http://127.0.0.1:8000/Comext_Export_GU_CVS?start=1998-01-01&end=1998-01-01&type=PRODUITS%20FINIS%20D%27EQUIPEMENT%20CVS-CJO
@api.get('/Comext_Export_GU_CVS')
def getComptes(start: str = '', end: str = '', type: str = ''):
    if (start and end and type):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_Export_GU_CVS.aggregate([{"$match": { "$and":[ {"date": {"$gte": start_date, "$lte": end_date}, "Type ": {"$eq": type}}]}}, {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, { "$project": {"_id": 0, "date": "$Date", "Type": "$Type ","Valeur": "$Valeur "}}])
    elif (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_Export_GU_CVS.aggregate([{"$match": {"date": {"$gte": start_date, "$lte": end_date}}}, {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, { "$project": {"_id": 0, "date": "$Date", "Type": "$Type ","Valeur": "$Valeur "}}])
    elif (type):
          b = Comext_Export_GU_CVS.aggregate([{"$match": {"Type ": {"$eq": type}}}, {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, { "$project": {"_id": 0, "date": "$Date", "Type": "$Type ","Valeur": "$Valeur "}}])
    else:
        b = Comext_Export_GU_CVS.aggregate([{"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}},{"$project": {"_id": 0, "date": "$Date", "Type": "$Type ", "Valeur": "$Valeur "}}])
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(b)))
##################################################################################################################
##############"################################Comext_TOTAL_CVS_CJO###############################################
@api.get('/Comext_TOTAL_CVS_CJO')
def getComptes(start: str = '', end: str = '', type: str = ''):
    if (start and end and type):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_TOTAL_CVS_CJO.aggregate([{"$match": { "$and":[ {"date": {"$gte": start_date, "$lte": end_date}, "Type ": {"$eq": type}}]}}, {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, { "$project": {"_id": 0, "date": "$Date", "Type": "$Type ","Valeur": "$valeur "}}])
    elif (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_TOTAL_CVS_CJO.aggregate([{"$match": {"date": {"$gte": start_date, "$lte": end_date}}}, {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, { "$project": {"_id": 0, "date": "$Date", "Type": "$donnees commerce exterieur","Valeur": "$valeur "}}])
    elif (type):
          b = Comext_TOTAL_CVS_CJO.aggregate([{"$match": {"Type ": {"$eq": type}}}, {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, { "$project": {"_id": 0, "date": "$Date", "Type": "$donnees commerce exterieur","Valeur": "$valeur "}}])
    else:
        b = Comext_TOTAL_CVS_CJO.aggregate([{"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$Date"}}}},{"$project": {"_id": 0, "date": "$Date", "Type": "$donnees commerce exterieur", "Valeur": "$valeur "}}])
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(b)))

###################################################################################################################
#############################
@api.get('/Comext_TOTAL_CVS_CJO') # ==> localhost:8080/Comext_TOTAL_CVS_CJO?start=1996-06-30&end=1999-01-01
def getComptes(start: str = '' , end: str = ''):
    if (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_TOTAL_CVS_CJO.aggregate([{"$match":{"Date":{"$gte": start_date, "$lte": end_date}}}, {"$addFields": {"date": {"$dateToString": { "format": "%Y-%m-%d", "date": "$Date" }} }}, { "$project" : {"_id" : 0 , "Date": "$date", "donnees commerce exterieur":"$donnees commerce exterieur", "valeur":"$valeur "}}])
    else:
        b = Comext_TOTAL_CVS_CJO.aggregate([{"$addFields": {"date": {"$dateToString": { "format": "%Y-%m-%d", "date": "$Date" }} }}, { "$project" : {"_id" : 0 , "Date": "$date", "donnees commerce exterieur":"$donnees commerce exterieur", "valeur":"$valeur "}}
        ])
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(b)))

###################################################################################################################


########################################################################################################
#####################Dep_Voyages_Nature_0#############################################################
@api.get('/Dep_Voyages_Nature_0')
def getComptes(start: int = '' , end: str = ''):
##########################Evol_MRE#########################= 0 , end: int = 0):
    if (start and end):
        a = list(Dep_Voyages_Nature_0.find({ "Date": {"$gte": start, "$lte": end} },{ "_id": 0, "Date": 1, "nature d'operation": 1, "valeur ": 1 }));
    else:
        a = list(Dep_Voyages_Nature_0.find({},{ "_id": 0, "Date": 1, "nature d'operation": 1,"valeur ": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
    ##########################################################################################################################

    ################################################Evol_MRE_3###############################################################

@api.get('/Evol_MRE_3')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(Evol_MRE_3.find({ "Date": {"$gte": start, "$lte": end} },{ "_id": 0, "Date": 1, "periode": 1, "Recette MRE": 1 }));
    else:
        a = list(Evol_MRE_3.find({},{ "_id": 0, "Date": 1, "periode": 1,"Recette MRE": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))

####################################################Evol_MRE_PAYS####################################################
@api.get('/Evol_MRE_PAYS')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(Evol_MRE_PAYS.find({ "DATE": {"$gte": start, "$lte": end} },{ "_id": 0, "DATE": 1, "PAYS": 1, "VALEUR": 1 }));
    else:
        a = list(Evol_MRE_PAYS.find({},{ "_id": 0, "DATE": 1, "PAYS": 1,"VALEUR": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
#####################################################################################################################
######################################Evol_MRe_CVS###################################################################


@api.get('/Evol_MRE_CVS') # ==> localhost:8080/vol?start=1996-06-30&end=1999-01-01
def getComptes(start: str = '' , end: str = ''):
    if (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Evol_MRE_CVS.aggregate([{"$match":{"date":{"$gte": start_date, "$lte": end_date}}}, {"$addFields": {"Date": {"$dateToString": { "format": "%Y-%m-%d", "date": "$date" }} }}, {"$project": {"_id": 0, "date": "$Date", "MRE":"$MRE" }},
        ])
    else:
        b = Evol_MRE_CVS.aggregate([{"$addFields": {"Date": {"$dateToString": { "format": "%Y-%m-%d", "date": "$date" }} }}, {"$project": {"_id": 0, "date": "$Date", "MRE":"$MRE" }}
        ])
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(b)))
    #################################################################################################################
    #####################################################################################################################
    ###########################Evol_Recettes_Voyages_5########################
@api.get('/Evol_Recettes_Voyages_5')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(Evol_Recettes_Voyages_5.find({ "Date": {"$gte": start, "$lte": end} },{ "_id": 0, "Date": 1, "Periode": 1, "Recettes Voyages": 1 }));
    else:
        a = list(Evol_Recettes_Voyages_5.find({},{ "_id": 0, "Date": 1, "Periode": 1,"Recettes Voyages": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
######################################################################################################################
############################################Evol_voyages_CVS#########################################################
@api.get('/Evol_voyages_CVS') # ==> localhost:8080/vol?start=1996-06-30&end=1999-01-01
def getComptes(start: str = '' , end: str = ''):
    if (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Evol_voyages_CVS.aggregate([{"$match":{"date ":{"$gte": start_date, "$lte": end_date}}}, {"$addFields": {"Date": {"$dateToString": { "format": "%Y-%m-%d", "date": "$date " }} }}, {"$project": {"_id": 0, "date": "$Date", "voyage":"$Voyages" }},
        ])
    else:
        b = Evol_voyages_CVS.aggregate([{"$addFields": {"Date": {"$dateToString": { "format": "%Y-%m-%d", "date": "$date " }} }}, {"$project": {"_id": 0, "date": "$Date", "voyage":"$Voyages", }}
        ])
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(b)))
####################################################################################################################
##########################IDE_Maroc_flux_Flux_nets_par_pays_0##################################
@api.get('/IDE_Maroc_flux_Flux_nets_par_pays_0')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_flux_Flux_nets_par_pays_0.find({ "Date ": {"$gte": start, "$lte": end} },{ "_id": 0, "Date ": 1, "PAYS/ORGANISMES FINANCIERS": 1, "Valeur": 1 }));
    else:
        a = list(IDE_Maroc_flux_Flux_nets_par_pays_0.find({},{ "_id": 0, "Date ": 1, "PAYS/ORGANISMES FINANCIERS": 1,"Valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
##############################################################################################################
############################################IDE_Maroc_stock_Par_secteurs######################################
@api.get('/IDE_Maroc_Stock_Par_secteurs')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Stock_Par_secteurs.find({ "Date": {"$gte": start, "$lte": end} },{ "_id": 0, "Date": 1, "Stock_IDEM_Pays": 1, "Valeur": 1 }));
    else:
        a = list(IDE_Maroc_Stock_Par_secteurs.find({},{ "_id": 0, "Date": 1, "Stock_IDEM_Pays": 1,"Valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
#######################################################################################################################
#############################################IDE_Maroc_Stock_Par_pays##############################################
@api.get('/IDE_Maroc_Stock_Par_pays')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Stock_Par_pays.find({ "Date": {"$gte": start, "$lte": end} },{ "_id": 0, "Date": 1, "Pays": 1, "valeur": 1 }));
    else:
        a = list(IDE_Maroc_Stock_Par_pays.find({},{ "_id": 0, "Date": 1, "Pays": 1,"valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
#########################################################################################################


#######################################IDE_Maroc_Recettes_par_Secteurs_NMA_0####################################
@api.get('/IDE_Maroc_Recettes_par_secteurs_NMA_0')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Recettes_par_secteurs_NMA_0.find({"Date": {"$gte": start, "$lte": end}},{"_id": 0, "Date": 1,"SECTEURS D'ACTIVITE": 1, "type": 1, "Valeur": 1,}));
    else:
        a = list(IDE_Maroc_Recettes_par_secteurs_NMA_0.find({}, {"_id": 0, "Date": 1,"SECTEURS D'ACTIVITE": 1,"type": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
    ##################################################################################################
    #########################IDE_Maroc_recettes_par_secteurs_0########################################
    ##################################################################################################
@api.get('/IDE_Maroc_Recettes_par_secteurs_0')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Recettes_par_secteurs_0.find({"Date": {"$gte": start, "$lte": end}},{"_id": 0, "Date": 1, "SECTEURS D'ACTIVITE": 1,"Valeur": 1}));
    else:
        a = list(IDE_Maroc_Recettes_par_secteurs_0.find({},{"_id": 0, "Date": 1, "SECTEURS D'ACTIVITE": 1,"Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

###############################################################################################################
#################################IDE_Maroc_Recettes_par_pays_0################################################
@api.get('/IDE_Maroc_Recettes_par_pays_0')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Recettes_par_pays_0.find({ "Date": {"$gte": start, "$lte": end} },{ "_id": 0, "Date": 1, "Pays ": 1, "Valeur": 1 }));
    else:
        a = list(IDE_Maroc_Recettes_par_pays_0.find({},{ "_id": 0, "Date": 1, "Pays ": 1,"Valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))

##########################################################################################################################
#################################IDE_Maroc_Flux_Par_Nature_opération_0###################################################

@api.get('/IDE_Maroc_Flux_Par_Nature_opération_0')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Flux_Par_Nature_opération_0.find({ "Date": {"$gte": start, "$lte": end} },{ "_id": 0, "Date": 1, "Nature d'operation": 1, "Type": 1, "Valeur": 1 }));
    else:
        a = list(IDE_Maroc_Flux_Par_Nature_opération_0.find({},{ "_id": 0, "Date": 1, "Nature d'operation": 1, "Type": 1,"Valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))

################################################################################################################
#####################################IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_0################################
@api.get('/IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_0')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_0.find({ "date ": {"$gte": start, "$lte": end} },{ "_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1, "type ": 1, "valeur": 1 }));
    else:
        a = list(IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_0.find({},{ "_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1, "type ": 1,"valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
####################################################################################################################
###################################IDM_a_Etranger_Flux_Depenses_par_pays_0##########################################
@api.get('/IDM_a_Etranger_Flux_Depenses_par_pays_0')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDM_a_Etranger_Flux_Depenses_par_pays_0.find({ "date ": {"$gte": start, "$lte": end} },{ "_id": 0, "date ": 1, "PAYS DE DESTINATION": 1, "Valeur": 1 }));
    else:
        a = list(IDM_a_Etranger_Flux_Depenses_par_pays_0.find({},{ "_id": 0, "date ": 1, "PAYS DE DESTINATION": 1,"Valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
#######################################################################################################################
#####################################IDM_a_Etranger_Flux_Depenses_par_secteurs_1#######################################
@api.get('/IDM_a_Etranger_Flux_Depenses_par_secteurs_1')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDM_a_Etranger_Flux_Depenses_par_secteurs_1.find({ "date ": {"$gte": start, "$lte": end} },{ "_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1, "valeur": 1 }));
    else:
        a = list(IDM_a_Etranger_Flux_Depenses_par_secteurs_1.find({},{ "_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1,"valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
######################################################################################################################
#################################IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0######################################
@api.get('/IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0.find({ "date": {"$gte": start, "$lte": end} },{ "_id": 0, "date": 1, "SECTEURS D'ACTIVITE": 1, "type": 1, "VALEUR": 1 }));
    else:
        a = list(IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0.find({},{ "_id": 0, "date": 1, "SECTEURS D'ACTIVITE": 1, "type": 1,"VALEUR": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
##################################################################################################################
###########################IDM_a_Etranger_Flux_Flux_nets_par_pays_0###############################################

@api.get('/IDM_a_Etranger_Flux_Flux_nets_par_pays_0')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDM_a_Etranger_Flux_Flux_nets_par_pays_0.find({ "Date": {"$gte": start, "$lte": end} },{ "_id": 0, "Date": 1, "PAYS DE DESTINATION": 1, "Valeur": 1 }));
    else:
        a = list(IDM_a_Etranger_Flux_Flux_nets_par_pays_0.find({},{ "_id": 0, "Date": 1, "PAYS DE DESTINATION": 1,"Valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
#####################################################################################################################
####################################IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_1#################################
@api.get('/IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_1')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_1.find({ "date ": {"$gte": start, "$lte": end} },{ "_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1, "type ":1, "valeur": 1 }));
    else:
        a = list(IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_1.find({},{ "_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1, "type ":1,"valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
#####################################################################################################################
###################################IDM_etranger_flux_par_nat_operation###############################################
@api.get('/IDM_etranger_flux_par_nat_operation')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDM_etranger_flux_par_nat_operation.find({ "Date ": {"$gte": start, "$lte": end} },{ "_id": 0, "Date ": 1, "Nature d'operation": 1, "operation":1, "valeur": 1 }));
    else:
        a = list(IDM_etranger_flux_par_nat_operation.find({},{ "_id": 0, "Date ": 1, "Nature d'operation": 1, "operation":1,"valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))

####################################################################################################################
 ################################IDM_a_etranger_Stock_Par_pays##################################################
@api.get('/IDM_a_etranger_Stock_Par_pays')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDM_a_etranger_Stock_Par_pays.find({ "Date": {"$gte": start, "$lte": end} },{ "_id": 0, "Date": 1, "PAYS": 1, "Valeur": 1 }));
    else:
        a = list(IDM_a_etranger_Stock_Par_pays.find({},{ "_id": 0, "Date": 1, "PAYS":1,"Valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))


#####################################################################################################################
#######################################IDM_à_etranger_Stock_Par_secteurs#############################################
    
@api.get('/IDM_à_etranger_Stock_Par_secteurs')
def getComptes(start: int = 0 , end: int = 0):
    if (start and end):
        a = list(IDM_à_etranger_Stock_Par_secteurs.find({ "Date": {"$gte": start, "$lte": end} },{ "_id": 0, "Date": 1, "SECTEURS": 1, "Valeur": 1 }));
    else:
        a = list(IDM_à_etranger_Stock_Par_secteurs.find({},{ "_id": 0, "Date": 1, "SECTEURS":1,"Valeur": 1 }));
    return JSONResponse(status_code=200 , content=json.loads(json_util.dumps(a)))
    ################################################################################################################
###################################

###############################################################################################################
#########################################Voyages_Pays_0#######################################################
@api.get('/Voyages_Pays_0')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Voyages_Pays_0.find({"Date": {"$gte": start, "$lte": end}}, {"_id": 0, "Date": 1, "Pays": 1, "Valeur": 1}));
    else:
        a = list(Voyages_Pays_0.find({}, {"_id": 0, "Date": 1, "Pays": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
##################################################################################################################
###########################IDM_a_etranger_Flux_Flux_nets_par_pays_0###############################################
@api.get('/IDM_a_etranger_Flux_Flux_nets_par_pays_0')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDM_a_etranger_Flux_Flux_nets_par_pays_0.find({"Date": {"$gte": start, "$lte": end}}, {"_id": 0, "Date": 1, "PAYS DE DESTINATION": 1, "Valeur": 1}));
    else:
        a = list(IDM_a_etranger_Flux_Flux_nets_par_pays_0.find({}, {"_id": 0, "Date": 1, "PAYS DE DESTINATION": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#####################################################################################################################
############################################Balance_Services_4#######################################################
@api.get('/Balance_Services_4')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Balance_Services_4.find({"Date": {"$gte": start, "$lte": end}}, {"_id": 0, "Date": 1, "Evolution des �changes de services": 1, "valeur": 1}));
    else:
        a = list(Balance_Services_4.find({}, {"_id": 0, "Date": 1, "Evolution des �changes de services": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

#######################################################################################################################
#########################################imp_services_nature_4_avant2014##############################################

@api.get('/imp_services_nature_4_avant2014')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(imp_services_nature_4_avant2014.find({"Date": {"$gte": start, "$lte": end}}, {"_id": 0, "Date": 1, "Importations": 1, "valeur": 1}));
    else:
        a = list(imp_services_nature_4_avant2014.find({}, {"_id": 0, "Date": 1, "Importations": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
######################################################################################################################
##################################Imp_Services_Nature_4_depuis2014####################################################
@api.get('/Imp_Services_Nature_4_depuis2014')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Imp_Services_Nature_4_depuis2014.find({"Date": {"$gte": start, "$lte": end}}, {"_id": 0, "Date": 1, "Importations": 1, "valeur": 1}));
    else:
        a = list(Imp_Services_Nature_4_depuis2014.find({}, {"_id": 0, "Date": 1, "Importations": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#######################################################################################################################
############################################Exp_services_nature_4_avant2014###########################################
@api.get('/Exp_services_nature_4_avant2014')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Exp_services_nature_4_avant2014.find({"date ": {"$gte": start, "$lte": end}}, {"_id": 0, "date ": 1, "Exportations": 1, "valeur": 1}));
    else:
        a = list(Exp_services_nature_4_avant2014.find({}, {"_id": 0, "date ": 1, "Exportations": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#######################################################################################################################
###########################################Exp_Services_Nature_4_depuis2014############################################
@api.get('/Exp_Services_Nature_4_depuis2014')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Exp_Services_Nature_4_depuis2014.find({"date": {"$gte": start, "$lte": end}}, {"_id": 0, "date": 1, "Exportations": 1, "valeur": 1}));
    else:
        a = list(Exp_Services_Nature_4_depuis2014.find({}, {"_id": 0, "date": 1, "Exportations": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
######################################################################################################################
#########################################Offshoring_3#################################################################
@api.get('/Offshoring_3')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Offshoring_3.find({"date": {"$gte": start, "$lte": end}}, {"_id": 0, "date": 1, "Periode": 1,"source": 1, "Type ":1, " valeur ": 1}));
    else:
        a = list(Offshoring_3.find({}, {"_id": 0, "date": 1, "Periode": 1,"source": 1, "Type ":1, " valeur ": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#####################################################################################################################
##################################BP_A_MBP5##########################################################################
@api.get('/BP_A_MBP5')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5.find({"Date": {"$gte": start, "$lte": end}}, {"_id": 0, "Date": 1, "Balance de paiement": 1,"Cat�gorie": 1, "Nature de l'op�ration":1, "valeur": 1}));
    else:
        a = list(BP_A_MBP5.find({}, {"_id": 0, "Date": 1,"Balance de paiement": 1,"Cat�gorie": 1, "Nature de l'op�ration":1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
######################################################################################################################
##########################################BP_A_MBP6_0#################################################################
@api.get('/BP_A_MBP6_0')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP6_0.find({"date": {"$gte": start, "$lte": end}}, {"_id": 0, "date": 1, "balance des paiements annuelle selon MBP6": 1,"cat�gorie": 1, "nature ":1, "valeur": 1}));
    else:
        a = list(BP_A_MBP6_0.find({}, {"_id": 0, "date": 1,"balance des paiements annuelle selon MBP6": 1,"cat�gorie": 1, "nature ":1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
######################################################################################################################
###################################################BP_T_MBP5##########################################################
@api.get('/BP_T_MBP5')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_T_MBP5.find({"date": {"$gte": start, "$lte": end}}, {"_id": 0, "date": 1, "periode": 1, "Balance des paiements trimestrielle selon MBP5": 1,"cat�gorie": 1, "nature ":1, "valeur": 1}));
    else:
        a = list(BP_T_MBP5.find({}, {"_id": 0, "date": 1,"periode": 1, "Balance des paiements trimestrielle selon MBP5": 1,"cat�gorie": 1, "nature ":1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#######################################################################################################################
##################################################BP_T_MBP6_3##########################################################
@api.get('/BP_T_MBP6_3')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_T_MBP6_3.find({"Date": {"$gte": start, "$lte": end}}, {"_id": 0, "Date": 1, "P�riode": 1, "Balance des paiements": 1,"Cat�gorie": 1, "Nature d'op�ration":1, "Valeur": 1}));
    else:
        a = list(BP_T_MBP6_3.find({}, {"_id": 0, "Date": 1,"P�riode": 1, "Balance des paiements": 1,"Cat�gorie": 1, "Nature d'op�ration":1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
