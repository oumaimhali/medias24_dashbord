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


client = MongoClient('mongodb://oumaima_hl:Oumaimamedias24@cluster0-shard-00-00.scaj4.mongodb.net:27017,cluster0-shard-00-01.scaj4.mongodb.net:27017,cluster0-shard-00-02.scaj4.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-wu1uy5-shard-0&authSource=admin&retryWrites=true&w=majority')

db = client['office_des_changes']

Voyages_Pays_0 = db.Voyages_Pays_0
compte_courant = db.compte_courant
Comext_import_GU_CVS = db.Comext_import_GU_CVS
Comext_Export_GU_CVS = db.Comext_Export_GU_CVS
Comext_TOTAL_CVS_CJO = db.Comext_TOTAL_CVS_CJO
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
IDM_a_etranger_Flux_Depenses_par_secteurs_1 = db.IDM_a_etranger_Flux_Depenses_par_secteurs_1
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
###############################################################################################################################################################################
###############################################################historique #################################################################################################
################################################################################################################################################################################

@api.get("/")
async def Historique ():
    Historique = [

    {
        "name": "Commerce extérieur",
        "elements": [
            {
                "name": "Les importations CVS",
                "url": "/Comext_import_GU_CVS/Historique"
            },
            {
                "name": "Les exportations CVS",
                "url": "/Comext_Export_GU_CVS/Historique"
            },
            {
                "name": "Total Commerce extérieur",
                "url": "/Comext_TOTAL_CVS_CJO/Historique"
            }
        ]
    },
    {
        "name": "Investissements internationaux",
        "elements": [
            {
                "name": "Investissements directs étrangers au Maroc",
                "elements":[
                    {
                        "name": "Flux",
                        "elements":[
                            {
                                "name": "Par nature d'opération",
                                "elements": [
                                    {
                                        "name": "Investissements directs étrangers au Maroc Flux Par nature d'opération",
                                        "url": "/IDE_Maroc_Flux_Par_Nature_opération_0/Historique"
                                    }
                                ]
                            },
                            {
                                "name": "Par pays",
                                "elements": [
                                    {
                                        "name": "Investissements directs étrangers au Maroc Recettes par pays",
                                        "url": "/IDE_Maroc_Recettes_par_pays_0/Historique"
                                    },
                                    {
                                        "name": "Investissements directs étrangers au Maroc flux Flux nets par pays",
                                        "url": "/IDE_Maroc_flux_Flux_nets_par_pays_0/Historique"
                                    }
                                ]
                            },
                            {
                                "name": "Par secteurs",
                                "elements": [
                                    {
                                        "name": "Investissements directs étrangers au Maroc Recettes par secteurs",
                                        "url": "/IDE_Maroc_Recettes_par_secteurs_0/Historique"
                                    },
                                    {
                                        "name": "Investissements directs étrangers au Maroc Recettes par secteurs NMA",
                                        "url": "/IDE_Maroc_Recettes_par_secteurs_NMA_0/Historique"
                                    },
                                    {
                                        "name": "Investissements directs étrangers au Maroc Flux flux nets par secteurs NMA",
                                        "url": "/IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_0/Historique"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "Stock",
                        "elements":[
                            {
                                "name": "Investissements directs étrangers au Maroc Stock Par pays",
                                "url": "/IDE_Maroc_Stock_Par_pays/Historique"
                            },
                            {
                                "name": "Investissements directs étrangers au Maroc Stock Par secteurs",
                                "url": "/IDE_Maroc_Stock_Par_secteurs/Historique"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Investissements directs marocains à l’étranger",
                "elements":[
                    {
                        "name": "Flux",
                        "elements":[
                            {
                                "name": "Par nature d'opération",
                                "elements": [
                                    {
                                        "name": "Investissements directs marocains à l’étranger flux par nature d'opération",
                                        "url": "/IDM_etranger_flux_par_nat_operation/Historique"
                                    }
                                ]
                            },
                            {
                                "name": "Par pays",
                                "elements": [
                                    {
                                        "name": "Investissements directs marocains à l’étranger Flux Dépenses par pays",
                                        "url": "/IDM_a_Etranger_Flux_Depenses_par_pays_0/Historique"
                                    },
                                    {
                                        "name": "Investissements directs marocains à l’étranger Flux Flux nets par pays",
                                        "url": "/IDM_a_etranger_Flux_Flux_nets_par_pays_0/Historique"
                                    }
                                ]
                            },
                            {
                                "name": "Par secteurs",
                                "elements": [
                                    {
                                        "name": "Investissements directs marocains à l’étranger Flux Depenses par secteurs",
                                        "url": "/IDM_a_etranger_Flux_Depenses_par_secteurs_1/Historique"
                                    },
                                    {
                                        "name": "Investissements directs marocains à l’étranger Flux Depenses par secteurs NMA",
                                        "url": "/IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0/Historique"
                                    },
                                    {
                                        "name": "Investissements directs marocains à l’étranger Flux Flux nets par secteurs NMA",
                                        "url": "/IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_1/Historique"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "Stock",
                        "elements":[
                            {
                                "name": "Par pays",
                                "elements":[
                                    {
                                        "name": "Investissements directs marocains à l’étranger Stock Par pays",
                                        "url": "/IDM_a_etranger_Stock_Par_pays/Historique"
                                    }
                                ]
                            },
                            {
                                "name": "Par pays",
                                "elements":[
                                    {
                                        "name": "Investissements directs marocains à l’étranger Stock Par secteurs",
                                        "url": "/IDM_à_etranger_Stock_Par_secteurs/Historique"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
        ]
    },
    {
        "name": "Balance des paiements et position extérieure globale",
        "elements": [
            {
                "name": "Etat de la Balance des paiements",
                "elements":[
                    {
                        "name":"Balance des paiements annuelle",
                        "elements":[
                            {
                                "name":"Balance des paiements annuelle selon MBP5",
                                "url":"/BP_A_MBP5/Historique"
                            },
                            {
                                "name":"Balance des paiements annuelle seleon MBP6",
                                "url":"/BP_A_MBP6_0/Historique"
                            }
                        ]
                    },
                    {
                        "name":"Balance des paiements trimestrielle",
                        "elements":[
                            {
                                "name":"Balance des paiements trimestrielle selon MBP5",
                                "url":"/BP_T_MBP5/Historique"
                            },
                            {
                                "name":"BP_T_MBP6_3",
                                "url":"/Balance des paiements trimestrielle selon MBP6/Historique"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Transactions courantes",
                "elements":[
                    {
                        "name":"compte_courant",
                        "url":"/compte_courant/Historique"
                    },
                    {
                        "name":"Les échanges de services",
                        "elements":[
                            {
                                "name":"Balance des Services",
                                "url":"/Balance_Services_4/Historique"
                            },
                            {
                                "name":"Importations des services nature avant 2014",
                                "url":"/imp_services_nature_4_avant2014/Historique"
                            },
                            {
                                "name":"Importations des services nature depuis 2014",
                                "url":"/Imp_Services_Nature_4_depuis2014/Historique"
                            },
                            {
                                "name":"Exportations des services nature avant 2014",
                                "url":"/Exp_services_nature_4_avant2014/Historique"
                            },
                            {
                                "name":"Exportations des services nature depuis 2014",
                                "url":"/Exp_Services_Nature_4_depuis2014/Historique"
                            },
                            {
                                "name":"Offshoring",
                                "url":"/Offshoring_3/Historique"
                            }
                        ]
                    },
                    {
                        "name":"Les voyages",
                        "elements":[
                            {
                                "name":"Recettes Voyages par pays",
                                "url":"/Voyages_Pays_0/Historique"
                            },
                            {
                                "name":"Evolution mensuelle des recettes Voyages",
                                "url":"/Evol_Recettes_Voyages_5/Historique"
                            },
                            {
                                "name":"Evolution annuelle des dépenses Voyages par nature d’opération",
                                "url":"/Dep_Voyages_Nature_0/Historique"
                            },
                            {
                                "name":"Evolution mensuelle des recettes Voyages CVS",
                                "url":"/Evol_voyages_CVS/Historique"
                            }
                        ]
                    },
                    {
                        "name":"Les recettes MRE",
                        "elements":[
                            {
                                "name":"Recettes MRE par pays",
                                "url":"/Evol_MRE_PAYS/Historique"
                            },
                            {
                                "name":"Evolution mensuelle des recettes MRE",
                                "url":"/Evol_MRE_3/Historique"
                            },
                            {
                                "name":"Evolution des recettes MRE CVS",
                                "url":"/Evol_MRE_CVS/Historique"
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
    return Historique


# list the collections =>
# for coll in db.list_collection_names():
#    stocker les collections dans une list
########################################################################################################################
##########################################compte_courant_hierarchy######################################################
########################################################################################################################
@api.get("/compte_courant/")
async def hierarchy():
    compte_courant_hierarchy=[

        {"name":"compte_courant",
        "elements":[

            ]
            },

    ]
    return compte_courant_hierarchy
########################################################################################################################"
########################################compte_courant_historique#########################################################

@api.get('/compte_courant/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(compte_courant.find({"date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "date": 1, "Solde du compte courant": 1}));
    else:
        a = list(compte_courant.find({}, {"_id": 0, "date": 1, "Solde du compte courant": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


######################################################################################################################
############################Comext_import_GU_CVS####################################################################
@api.get('/Comext_import_GU_CVS/Historique')
def getComptes(start: str = '', end: str = '', type: str = ''):
    if (start and end and type):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_import_GU_CVS.aggregate(
            [{"$match": {"$and": [{"date": {"$gte": start_date, "$lte": end_date}, "Type ": {"$eq": type}}]}},
             {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}},
             {"$project": {"_id": 0, "date": "$Date", "Type": "$Type ", "Valeur": "$Valeur "}}])
    elif (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_import_GU_CVS.aggregate([{"$match": {"date": {"$gte": start_date, "$lte": end_date}}}, {
            "$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, {
                                                "$project": {"_id": 0, "date": "$Date", "Type": "$Type ",
                                                             "Valeur": "$Valeur "}}])
    elif (type):
        b = Comext_import_GU_CVS.aggregate([{"$match": {"Type ": {"$eq": type}}}, {
            "$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, {
                                                "$project": {"_id": 0, "date": "$Date", "Type": "$Type ",
                                                             "Valeur": "$Valeur "}}])
    else:
        b = Comext_import_GU_CVS.aggregate(
            [{"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}},
             {"$project": {"_id": 0, "date": "$Date", "Type": "$Type ", "Valeur": "$Valeur "}}])
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(b)))


####################################################################################################################

####################################################################################################################
#######################################Comext_export_GU_CVS-CJO######################################################
# url ==> http://127.0.0.1:8000/Comext_Export_GU_CVS?start=1998-01-01&end=1998-01-01&type=PRODUITS%20FINIS%20D%27EQUIPEMENT%20CVS-CJO
@api.get('/Comext_Export_GU_CVS/Historique')
def getComptes(start: str = '', end: str = '', type: str = ''):
    if (start and end and type):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_Export_GU_CVS.aggregate(
            [{"$match": {"$and": [{"date": {"$gte": start_date, "$lte": end_date}, "Type ": {"$eq": type}}]}},
             {"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}},
             {"$project": {"_id": 0, "date": "$Date", "Type": "$Type ", "Valeur": "$Valeur "}}])
    elif (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_Export_GU_CVS.aggregate([{"$match": {"date": {"$gte": start_date, "$lte": end_date}}}, {
            "$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, {
                                                "$project": {"_id": 0, "date": "$Date", "Type": "$Type ",
                                                             "Valeur": "$Valeur "}}])
    elif (type):
        b = Comext_Export_GU_CVS.aggregate([{"$match": {"Type ": {"$eq": type}}}, {
            "$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}}, {
                                                "$project": {"_id": 0, "date": "$Date", "Type": "$Type ",
                                                             "Valeur": "$Valeur "}}])
    else:
        b = Comext_Export_GU_CVS.aggregate(
            [{"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}},
             {"$project": {"_id": 0, "date": "$Date", "Type": "$Type ", "Valeur": "$Valeur "}}])
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(b)))


##################################################################################################################



###############################################Comext_TOTAL_CVS_CJO####################################################################

@api.get('/Comext_TOTAL_CVS_CJO/Historique')
def getComptes(start: str = '', end: str = '', type: str = ''):
    if (start and end and type):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_TOTAL_CVS_CJO.aggregate(
            [{"$match": {"$and": [{"Date": {"$gte": start_date, "$lte": end_date}, "donnees commerce exterieur": {"$eq": type}}]}},
             {"$addFields": {"date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$Date"}}}},
             {"$project": {"_id": 0, "date": "$date", "Type": "$donnees commerce exterieur", "Valeur": "$valeur "}}])
    elif (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Comext_TOTAL_CVS_CJO.aggregate([{"$match": {"Date": {"$gte": start_date, "$lte": end_date}}}, {
            "$addFields": {"date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$Date"}}}}, {
                                                "$project": {"_id": 0, "date": "$date",
                                                             "Type": "$donnees commerce exterieur",
                                                             "Valeur": "$valeur "}}])
    elif (type):
        b = Comext_TOTAL_CVS_CJO.aggregate([{"$match": {"donnees commerce exterieur": {"$eq": type}}}, {
            "$addFields": {"date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$Date"}}}}, {
                                                "$project": {"_id": 0, "date": "$date",
                                                             "Type": "$donnees commerce exterieur",
                                                             "Valeur": "$valeur "}}])
    else:
        b = Comext_TOTAL_CVS_CJO.aggregate(
            [{"$addFields": {"date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$Date"}}}},
             {"$project": {"_id": 0, "date": "$date", "Type": "$donnees commerce exterieur", "Valeur": "$valeur "}}])
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(b)))

##############################################################################################################################
##################################################Dep_Voyages_Nature_hierarchy###############################################
#############################################################################################################################

@api.get("/Dep_Voyages_Nature/")
async def hierarchy():
    Dep_Voyages_Nature_hierarchy=[

        {"name":"Nature d'opération",
        "elements":[
            {"name":"TOURISME","elements": []},
            {"name": "SCOLARITES", "elements": []},
            {"name": "VOYAGES D'AFFAIRES", "elements": []},
            {"name": "PELERINAGE ET OMRA", "elements": []},
            {"name": "STAGES ET MISSIONS", "elements": []},
            {"name": "SOINS MEDICAUX", "elements": []},
            {"name": "AUTRES VOYAGES", "elements": []}

            ]
            },
        {"name": "Valeur en MDH","elements": []}

    ]
    return Dep_Voyages_Nature_hierarchy
########################################################################################################
#####################Dep_Voyages_Nature_0_historique#############################################################
@api.get('/Dep_Voyages_Nature_0/Historique')
def getComptes(start: int = '', end: str = ''):
  
    if (start and end):
        a = list(Dep_Voyages_Nature_0.find({"Date": {"$gte": start, "$lte": end}},
                                           {"_id": 0, "Date": 1, "nature d'operation ": 1, "valeur ": 1}));
    else:
        a = list(Dep_Voyages_Nature_0.find({}, {"_id": 0, "Date": 1, "nature d'operation ": 1, "valeur ": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
    ###############################################################################################################
################################################Evol_MRE_3_hierarchy####################################################
###################################################################################################################
@api.get("/Evol_MRE/")
async def hierarchy():
    Evol_MRE_hierarchy=[

        {"name":"periode",
        "elements":[
            {"name":"Janvier","elements": []},
            {"name": "Février", "elements": []},
            {"name": "Mars", "elements": []},
            {"name": "Avril", "elements": []},
            {"name": "Mai", "elements": []},
            {"name": "Juin", "elements": []},
            {"name": "Juillet", "elements": []},
            {"name": "Août", "elements": []},
            {"name": "Septembre", "elements": []},
            {"name": "Octobre", "elements": []},
            {"name": "Novembre", "elements": []},
            {"name": "Décembre", "elements": []}

            ]
            },
        {"name": "Recette MRE","elements": []}

    ]
    return Evol_MRE_hierarchy
    ###############################################################################################################
    ###############################################Evol_MRE_3/Historique#############################################
    ##################################################################################################################


@api.get('/Evol_MRE_3/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Evol_MRE_3.find({"Date": {"$gte": start, "$lte": end}},
                                 {"_id": 0, "Date": 1, "periode": 1, "Recette MRE": 1}));
    else:
        a = list(Evol_MRE_3.find({}, {"_id": 0, "Date": 1, "periode": 1, "Recette MRE": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
######################################################################################################################
#########################################EVOL_MRE_PAYS_hierarchy#####################################################
#######################################################################################################################
@api.get("/Evol_MRE_Pays/")
async def hierarchy():
    Evol_MRE_Pays_hierarchy=[

        {"name":"PAYS",
        "elements":[
            {"name":"FRANCE","elements": []},
            {"name": "ITALIE", "elements": []},
            {"name": "ESPAGNE", "elements": []},
            {"name": "ARABIE SAOUDITE", "elements": []},
            {"name": "EMIRATS ARABES UNIS", "elements": []},
            {"name": "ETATS-UNIS", "elements": []},
            {"name": "BELGIQUE", "elements": []},
            {"name": "ALLEMAGNE", "elements": []},
            {"name": "PAYS-BAS", "elements": []},
            {"name": "Royaume-Uni", "elements": []},
            {"name": "QATAR", "elements": []},
            {"name": "KOWEIT", "elements": []},
            {"name": "SUISSE", "elements": []},
            {"name": "CANADA", "elements": []},
            {"name": "OMAN", "elements": []},
            {"name": "NORVEGE", "elements": []},
            {"name": "BAHREIN", "elements": []},
            {"name": "IRLANDE", "elements": []},
            {"name": "SUEDE", "elements": []},
            {"name": "DANEMARK", "elements": []},
            {"name": "Autres Pays", "elements": []}
            ]
            },
        {"name": "VALEUR","elements": []}
    ]
    return Evol_MRE_Pays_hierarchy

######################################################################################################################
####################################################Evol_MRE_PAYS####################################################
#######################################################################################################################
@api.get('/Evol_MRE_PAYS/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(
            Evol_MRE_PAYS.find({"DATE": {"$gte": start, "$lte": end}}, {"_id": 0, "DATE": 1, "PAYS": 1, "VALEUR": 1}));
    else:
        a = list(Evol_MRE_PAYS.find({}, {"_id": 0, "DATE": 1, "PAYS": 1, "VALEUR": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#####################################################################################################################
#######################################Evol_MRE_CVS##################################################################
#####################################################################################################################
@api.get("/Evol_MRE_CVS/")
async def hierarchy():
    Evol_MRE_CVS_hierarchy = [

        {"name": "MRE",
         "elements": [

         ]
         },

    ]
    return Evol_MRE_CVS_hierarchy


#####################################################################################################################
######################################Evol_MRe_CVS###################################################################


@api.get('/Evol_MRE_CVS/Historique')  # ==> localhost:8080/vol?start=1996-06-30&end=1999-01-01
def getComptes(start: str = '', end: str = ''):
    if (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Evol_MRE_CVS.aggregate([{"$match": {"date": {"$gte": start_date, "$lte": end_date}}}, {
            "$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}},
                                    {"$project": {"_id": 0, "date": "$Date", "MRE": "$MRE"}},
                                    ])
    else:
        b = Evol_MRE_CVS.aggregate(
            [{"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}}},
             {"$project": {"_id": 0, "date": "$Date", "MRE": "$MRE"}}
             ])
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(b)))
    #####################################################################################################################
    ##########################################Evol_Recettes_Voyages_historique###########################################
    #####################################################################################################################
@api.get("/Evol_Recettes_Voyages/")
async def hierarchy():
        Evol_Recettes_Voyages_hierarchy = [

         
            {"name": "Recettes Voyages", "elements": []}

        ]
        return Evol_Recettes_Voyages_hierarchy
    #####################################################################################################################
    ###########################Evol_Recettes_Voyages_5###################################################################


@api.get('/Evol_Recettes_Voyages_5/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Evol_Recettes_Voyages_5.find({"Date": {"$gte": start, "$lte": end}},
                                              {"_id": 0, "Date": 1, "Periode": 1, "Recettes Voyages": 1}));
    else:
        a = list(Evol_Recettes_Voyages_5.find({}, {"_id": 0, "Date": 1, "Periode": 1, "Recettes Voyages": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

###############################################################################################################################
#####################################################Evol_voyages_CVS_hierarchy################################################
###############################################################################################################################
@api.get("/Evol_voyages_CVS/")
async def hierarchy():
    Evol_voyages_CVS_hierarchy=[

        {"name":"Voyages",
        "elements":[

            ]
            },

    ]
    return Evol_voyages_CVS_hierarchy
###############################################################################################################################
############################################Evol_voyages_CVS_historique#########################################################
@api.get('/Evol_voyages_CVS/Historique')  # ==> localhost:8080/vol?start=1996-06-30&end=1999-01-01
def getComptes(start: str = '', end: str = ''):
    if (start and end):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        b = Evol_voyages_CVS.aggregate([{"$match": {"date ": {"$gte": start_date, "$lte": end_date}}}, {
            "$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date "}}}},
                                        {"$project": {"_id": 0, "date": "$Date", "voyage": "$Voyages"}},
                                        ])
    else:
        b = Evol_voyages_CVS.aggregate(
            [{"$addFields": {"Date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date "}}}},
             {"$project": {"_id": 0, "date": "$Date", "voyage": "$Voyages", }}
             ])
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(b)))


####################################################################################################################
##########################IDE_Maroc_flux_Flux_nets_par_pays_0##################################
@api.get('/IDE_Maroc_flux_Flux_nets_par_pays_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_flux_Flux_nets_par_pays_0.find({"Date ": {"$gte": start, "$lte": end}},
                                                          {"_id": 0, "Date ": 1, "PAYS/ORGANISMES FINANCIERS": 1,
                                                           "Valeur": 1}));
    else:
        a = list(IDE_Maroc_flux_Flux_nets_par_pays_0.find({}, {"_id": 0, "Date ": 1, "PAYS/ORGANISMES FINANCIERS": 1,
                                                               "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


##############################################################################################################
############################################IDE_Maroc_stock_Par_secteurs######################################
@api.get('/IDE_Maroc_Stock_Par_secteurs/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Stock_Par_secteurs.find({"Date": {"$gte": start, "$lte": end}},
                                                   {"_id": 0, "Date": 1, "Stock_IDEM_Pays": 1, "Valeur": 1}));
    else:
        a = list(IDE_Maroc_Stock_Par_secteurs.find({}, {"_id": 0, "Date": 1, "Stock_IDEM_Pays": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


#######################################################################################################################
#############################################IDE_Maroc_Stock_Par_pays##############################################
@api.get('/IDE_Maroc_Stock_Par_pays/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Stock_Par_pays.find({"Date": {"$gte": start, "$lte": end}},
                                               {"_id": 0, "Date": 1, "Pays": 1, "valeur": 1}));
    else:
        a = list(IDE_Maroc_Stock_Par_pays.find({}, {"_id": 0, "Date": 1, "Pays": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


#########################################################################################################


#######################################IDE_Maroc_Recettes_par_Secteurs_NMA_0####################################
@api.get('/IDE_Maroc_Recettes_par_secteurs_NMA_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Recettes_par_secteurs_NMA_0.find({"Date": {"$gte": start, "$lte": end}},
                                                            {"_id": 0, "Date": 1, "SECTEURS D'ACTIVITE": 1, "type": 1,
                                                             "Valeur": 1, }));
    else:
        a = list(IDE_Maroc_Recettes_par_secteurs_NMA_0.find({},
                                                            {"_id": 0, "Date": 1, "SECTEURS D'ACTIVITE": 1, "type": 1,
                                                             "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
    #################################################################################################################################################"
    #########################IDE_Maroc_recettes_par_secteurs_0#######################################################################################
    ######################################################################################################################################################


@api.get('/IDE_Maroc_Recettes_par_secteurs_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Recettes_par_secteurs_0.find({"Date": {"$gte": start, "$lte": end}},
                                                        {"_id": 0, "Date": 1, "SECTEURS D'ACTIVITE": 1, "Valeur": 1}));
    else:
        a = list(
            IDE_Maroc_Recettes_par_secteurs_0.find({}, {"_id": 0, "Date": 1, "SECTEURS D'ACTIVITE": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


###############################################################################################################
#################################IDE_Maroc_Recettes_par_pays_0################################################
@api.get('/IDE_Maroc_Recettes_par_pays_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Recettes_par_pays_0.find({"Date": {"$gte": start, "$lte": end}},{"_id": 0, "Date": 1, "Pays ": 1, "Valeur": 1}));
    else:
        a = list(IDE_Maroc_Recettes_par_pays_0.find({}, {"_id": 0, "Date": 1, "Pays ": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


##########################################################################################################################
#################################IDE_Maroc_Flux_Par_Nature_opération_0###################################################

@api.get('/IDE_Maroc_Flux_Par_Nature_opération_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Flux_Par_Nature_opération_0.find({"Date": {"$gte": start, "$lte": end}},
                                                            {"_id": 0, "Date": 1, "Nature d'operation": 1, "Type": 1,
                                                             "Valeur": 1}));
    else:
        a = list(IDE_Maroc_Flux_Par_Nature_opération_0.find({},
                                                            {"_id": 0, "Date": 1, "Nature d'operation": 1, "Type": 1,
                                                             "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


##################################################################################################################################
#####################################IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_0###################################################
@api.get('/IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_0.find({"date ": {"$gte": start, "$lte": end}},
                                                                  {"_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1,
                                                                   "type ": 1, "Valeur": 1}));
    else:
        a = list(IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_0.find({}, {"_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1,
                                                                       "type ": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


####################################################################################################################
###################################IDM_a_Etranger_Flux_Depenses_par_pays_0##########################################
@api.get('/IDM_a_Etranger_Flux_Depenses_par_pays_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDM_a_Etranger_Flux_Depenses_par_pays_0.find({"date ": {"$gte": start, "$lte": end}},
                                                              {"_id": 0, "date ": 1, "PAYS DE DESTINATION": 1,
                                                               "Valeur": 1}));
    else:
        a = list(IDM_a_Etranger_Flux_Depenses_par_pays_0.find({}, {"_id": 0, "date ": 1, "PAYS DE DESTINATION": 1,
                                                                   "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


#######################################################################################################################
#####################################IDM_a_Etranger_Flux_Depenses_par_secteurs_1#######################################
@api.get('/IDM_a_etranger_Flux_Depenses_par_secteurs_1/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDM_a_etranger_Flux_Depenses_par_secteurs_1.find({"date ": {"$gte": start, "$lte": end}},
                                                                  {"_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1,
                                                                   "valeur": 1}));
    else:
        a = list(IDM_a_etranger_Flux_Depenses_par_secteurs_1.find({}, {"_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1,
                                                                       "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


######################################################################################################################
#################################IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0######################################
@api.get('/IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0.find({"date": {"$gte": start, "$lte": end}},
                                                                      {"_id": 0, "date": 1, "SECTEURS D'ACTIVITE": 1,
                                                                       "type": 1, "VALEUR": 1}));
    else:
        a = list(IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_0.find({},
                                                                      {"_id": 0, "date": 1, "SECTEURS D'ACTIVITE": 1,
                                                                       "type": 1, "VALEUR": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


##################################################################################################################
###########################IDM_a_Etranger_Flux_Flux_nets_par_pays_0###############################################

@api.get('/IDM_a_Etranger_Flux_Flux_nets_par_pays_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDM_a_Etranger_Flux_Flux_nets_par_pays_0.find({"Date": {"$gte": start, "$lte": end}},
                                                               {"_id": 0, "Date": 1, "PAYS DE DESTINATION": 1,
                                                                "Valeur": 1}));
    else:
        a = list(IDM_a_Etranger_Flux_Flux_nets_par_pays_0.find({}, {"_id": 0, "Date": 1, "PAYS DE DESTINATION": 1,
                                                                    "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


#####################################################################################################################
####################################IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_1#################################
@api.get('/IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_1/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_1.find({"date ": {"$gte": start, "$lte": end}},
                                                                       {"_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1,
                                                                        "type ": 1, "valeur": 1}));
    else:
        a = list(IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_1.find({},
                                                                       {"_id": 0, "date ": 1, "SECTEURS D'ACTIVITE": 1,
                                                                        "type ": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


#####################################################################################################################
###################################IDM_etranger_flux_par_nat_operation###############################################
@api.get('/IDM_etranger_flux_par_nat_operation/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDM_etranger_flux_par_nat_operation.find({"Date": {"$gte": start, "$lte": end}},
                                                          {"_id": 0, "Date": 1, "Nature d'operation": 1, "operation": 1,
                                                           "valeur": 1}));
    else:
        a = list(IDM_etranger_flux_par_nat_operation.find({},
                                                          {"_id": 0, "Date": 1, "Nature d'operation": 1, "operation": 1,
                                                           "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


####################################################################################################################
################################IDM_a_etranger_Stock_Par_pays##################################################
@api.get('/IDM_a_etranger_Stock_Par_pays/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDM_a_etranger_Stock_Par_pays.find({"Date": {"$gte": start, "$lte": end}},
                                                    {"_id": 0, "Date": 1, "PAYS": 1, "Valeur": 1}));
    else:
        a = list(IDM_a_etranger_Stock_Par_pays.find({}, {"_id": 0, "Date": 1, "PAYS": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


#####################################################################################################################
#######################################IDM_à_etranger_Stock_Par_secteurs#############################################

@api.get('/IDM_à_etranger_Stock_Par_secteurs/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDM_à_etranger_Stock_Par_secteurs.find({"Date": {"$gte": start, "$lte": end}},
                                                        {"_id": 0, "Date": 1, "SECTEURS": 1, "Valeur": 1}));
    else:
        a = list(IDM_à_etranger_Stock_Par_secteurs.find({}, {"_id": 0, "Date": 1, "SECTEURS": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
    ################################################################################################################


 ################################################################################################################
###################################Voyages_Pays_hierarchy###########################################################
#####################################################################################################################
@api.get("/Voyages_Pays/")
async def hierarchy():
    Voyages_Pays_hierarchy = [

        {"name": "Pays",
         "elements": [
             {"name": "FRANCE", "elements": []},
             {"name": "ESPAGNE", "elements": []},
             {"name": "ROYAUME-UNI", "elements": []},
             {"name": "ALLEMAGNE", "elements": []},
             {"name": "ITALIE", "elements": []},
             {"name": "ÉTATS-UNIS", "elements": []},
             {"name": "BELGIQUE", "elements": []},
             {"name": "ARABIE SAOUDITE", "elements": []},
             {"name": "PAYS-BAS", "elements": []},
             {"name": "ÉMIRATS ARABES UNIS", "elements": []},
             {"name": "CANADA", "elements": []},
             {"name": "SUISSE", "elements": []},
             {"name": "CHINE", "elements": []},
             {"name": "ALGÉRIE", "elements": []},
             {"name": "POLOGNE", "elements": []},
             {"name": "SÉNÉGAL", "elements": []},
             {"name": "SUÈDE", "elements": []},
             {"name": "RUSSIE", "elements": []},
             {"name": "Autres pays", "elements": []}

         ]
         },
        {"name": "Valeur en MDH", "elements": []}

    ]
    return Voyages_Pays_hierarchy

###############################################################################################################
#########################################Voyages_Pays_0#######################################################
@api.get('/Voyages_Pays_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(
            Voyages_Pays_0.find({"Date": {"$gte": start, "$lte": end}}, {"_id": 0, "Date": 1, "Pays": 1, "Valeur": 1}));
    else:
        a = list(Voyages_Pays_0.find({}, {"_id": 0, "Date": 1, "Pays": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


##################################################################################################################
###########################IDM_a_etranger_Flux_Flux_nets_par_pays_0###############################################
@api.get('/IDM_a_etranger_Flux_Flux_nets_par_pays_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDM_a_etranger_Flux_Flux_nets_par_pays_0.find({"Date": {"$gte": start, "$lte": end}},
                                                               {"_id": 0, "Date": 1, "PAYS DE DESTINATION": 1,
                                                                "Valeur": 1}));
    else:
        a = list(IDM_a_etranger_Flux_Flux_nets_par_pays_0.find({}, {"_id": 0, "Date": 1, "PAYS DE DESTINATION": 1,
                                                                    "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

####################################################################################################################
######################################Balance_Services_hierarchy####################################################
######################################################################################################################
@api.get("/Balance_Services/")
async def hierarchy():
    Balance_Services_hierarchy=[

        {"name": "Evolution des échanges de services",
         "elements": [
             {"name": "Importations de services", "elements": []},
             {"name": "Exportations d services", "elements": []},
         ]
         },
        {"name": "Valeur en MDH", "elements": []}

    ]
    return Balance_Services_hierarchy
#####################################################################################################################
############################################Balance_Services_4#######################################################
@api.get('/Balance_Services_4/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Balance_Services_4.find({"Date": {"$gte": start, "$lte": end}},
                                         {"_id": 0, "Date": 1, "Evolution des �changes de services": 1, "valeur": 1}));
    else:
        a = list(
            Balance_Services_4.find({}, {"_id": 0, "Date": 1, "Evolution des �changes de services": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


#######################################################################################################################
#########################################imp_services_nature_4_avant2014##############################################

@api.get('/imp_services_nature_4_avant2014/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(imp_services_nature_4_avant2014.find({"Date": {"$gte": start, "$lte": end}},
                                                      {"_id": 0, "Date": 1, "Importations": 1, "valeur": 1}));
    else:
        a = list(imp_services_nature_4_avant2014.find({}, {"_id": 0, "Date": 1, "Importations": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


######################################################################################################################
##################################Imp_Services_Nature_4_depuis2014####################################################
@api.get('/Imp_Services_Nature_4_depuis2014/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Imp_Services_Nature_4_depuis2014.find({"Date": {"$gte": start, "$lte": end}},
                                                       {"_id": 0, "Date": 1, "Importations": 1, "valeur": 1}));
    else:
        a = list(Imp_Services_Nature_4_depuis2014.find({}, {"_id": 0, "Date": 1, "Importations": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


#######################################################################################################################
############################################Exp_services_nature_4_avant2014###########################################
@api.get('/Exp_services_nature_4_avant2014/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Exp_services_nature_4_avant2014.find({"date ": {"$gte": start, "$lte": end}},
                                                      {"_id": 0, "date ": 1, "Exportations": 1, "valeur": 1}));
    else:
        a = list(Exp_services_nature_4_avant2014.find({}, {"_id": 0, "date ": 1, "Exportations": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


#######################################################################################################################
###########################################Exp_Services_Nature_4_depuis2014############################################
@api.get('/Exp_Services_Nature_4_depuis2014/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Exp_Services_Nature_4_depuis2014.find({"date": {"$gte": start, "$lte": end}},
                                                       {"_id": 0, "date": 1, "Exportations": 1, "valeur": 1}));
    else:
        a = list(Exp_Services_Nature_4_depuis2014.find({}, {"_id": 0, "date": 1, "Exportations": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
@api.get("/Offshoring/")
async def hierarchy():
    Offshoring_hierarchy=[

        {"name": "segments",
         "elements": [
             {"name": "Engineering Services Outsourcing", "elements": []},
             {"name": "Knowledge Process Outsourcing", "elements": []}
         ]
         },
        {"name": " écosysytèmes",
         "elements": [
             {"name": "Customer Relationship Management", "elements": []},
             {"name": "Information Technology Outsourcing", "elements": []},
             {"name": "Business Process Outsourcing", "elements": []},
             {"name": "Engineering Services Outsourcing", "elements": []},
             {"name": "Knowledge Process Outsourcing", "elements": []},
         ]},
    ]
    return Offshoring_hierarchy

######################################################################################################################
#########################################Offshoring_3#################################################################
@api.get('/Offshoring_3/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Offshoring_3.find({"date": {"$gte": start, "$lte": end}},
                                   {"_id": 0, "date": 1, "Periode": 1, "source": 1, "Type ": 1, " valeur ": 1}));
    else:
        a = list(Offshoring_3.find({}, {"_id": 0, "date": 1, "Periode": 1, "source": 1, "Type ": 1, " valeur ": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
########################################################################################################################
#############################################BP_A_MBP5_Hiérarchie################################################################################
########################################################################################################################
@api.get("/BP_A_MBP5/")
async def hierarchy():
    BP_A_MBP5_hierarchy=[

        {"name":"SOLDE",
        "elements":[
            {"name":"COMPTE DES TRANSACTIONS COURANTES",
             "elements": [
                 {"name": "BIENS", "elements": []},
                 {"name": "SERVICES", "elements": []},
                 {"name": "REVENUS", "elements": []},
                 {"name": "TRANSFERTS COURANTS", "elements": []},
                 {"name": "INVESTISSEMENTS DIRECTS", "elements": []},
                 {"name": "INVESTISSEMENTS DE PORTEFEUILLE", "elements": []},
                 {"name": "AUTRES INVESTISSEMENTS", "elements": []},
                 {"name": "AVOIRS DE RÉSERVE", "elements": []}
                ]
            }
        ]},
        {"name": "CREDIT",
        "elements": [
            {"name": "COMPTE DES TRANSACTIONS COURANTES",
            "elements": [
                {"name": "BIENS",
                "elements": [
                    {"name" : "Marchandises générales", "elements": []},
                    {"name" : "Biens importés sans paiement et réexportés après transformation", "elements": []},
                    {"name" : "Achats de biens dans les ports", "elements": []},
                    ]
                },
                {"name": "SERVICES",
                "elements": [
                    {"name": "Transports",
                    "elements": [
                        {"name": "Transports maritimes", "elements": []},
                        {"name": "Transports aériens", "elements": []},
                        {"name": "Autres transports", "elements": []},
                        ]
                    },
                    {"name": "Voyages",
                    "elements": [
                        {"name": "Voyages à titre professionnel", "elements": []},
                        {"name": "Voyages à titre personnel", "elements": []}
                        ]
                    },
                    {"name": "Services de communication", "elements": []},
                    {"name": "Services d'assurance", "elements": []},
                    {"name": "Redevances et droits de licence", "elements": []},
                    {"name": "Autres services aux entreprises", "elements": []},
                    {"name": "Services fournis ou reçus par les administrations publiques N.C.A", "elements": []}
                ]},
                {"name": "REVENUS",
                "elements": [
                    {"name": "Administrations", "elements": []},
                    {"name": "Autorités monétaires", "elements": []},
                    {"name": "Banques", "elements": []},
                    {"name": "Autres secteurs", "elements": []},
                    ]
                },
                {"name": "TRANSFERTS COURANTS",
                "elements": [
                    {"name": "Publics", "elements": []},
                    {"name": "Privés", "elements": []}
                    ]
                }
            ]}
        ]},
        {"name": "DEBIT",
        "elements": [
            {"name": "COMPTE DES TRANSACTIONS COURANTES ",
            "elements": [
                {"name": "BIENS",
                "elements": [
                    {"name": "Marchandises générales", "elements": []},
                    {"name": "Biens importés sans paiement et réexportés après transformation", "elements": []},
                    {"name": "Achats de biens dans les ports", "elements": []}
                    ]
                },
                {"name": "SERVICES",
                "elements": [
                    {"name": "Transports",
                    "elements": [
                        {"name": "Transports maritimes", "elements":[]},
                        {"name": "Transports aériens", "elements": []},
                        {"name": "Autres transports", "elements": []},
                        ]
                    },
                    {"name": "Voyages",
                    "elements": [
                        {"name": "Voyages à titre professionnel", "elements":[]},
                        {"name": "Voyages à titre personnel", "elements":[]},
                    ]},
                    {"name": "Services de communication", "elements": []},
                    {"name": "Services d'assurance", "elements": []},
                    {"name": "Redevances et droits de licence", "elements": []},
                    {"name": "Autres services aux entreprises", "elements": []},
                    {"name": "Services fournis ou reçus par les administrations publiques N.C.A", "elements": []}
                ]},
                {"name": "REVENUS",
                "elements": [
                    {"name": "Administrations", "elements": []},
                    {"name": "Autorités monétaires", "elements": []},
                    {"name": "Banques", "elements": []},
                    {"name": "Autres secteurs", "elements": []},
                    ]
                },
                {"name": "TRANSFERTS COURANTS",
                "elements": [
                    {"name": "Publics", "elements": []},
                    {"name": "Privés", "elements": []}
                    ]
                }
            ]}
        ]},
        {"name": "CREDIT",
        "elements":[
            {"name":"COMPTE DES OPERATIONS FINANCIERES",
            "elements":[
                {"name": "Investissements directs",
                "elements": [
                    {"name": "A l'étranger", "elements": []},
                    {"name": "Dans l' économie nationale", "elements": []}
                    ]
                },
                {"name": "Investissements de portefeuille", "elements": [
                    {"name": "Avoirs", "elements": []},
                    {"name": "Engagements", "elements": []}
                    ]
                },
                {"name": "Autres investissements",
                "elements": [
                    {"name": "Crédits commerciaux",
                    "elements": [
                        {"name": "Autres secteurs", "elements": []}
                    ]},
                    {"name": "Prêts",
                    "elements": [
                        {"name": "Administrations","elements": []},
                        {"name": "Banques","elements": []},
                        {"name": "Autres secteurs","elements": []},
                    ]},
                    {"name": "Monnaie fiduciaire et dépôts","elements": []},
                    {"name": "Autres OF","elements": []},
                ]},
                {"name": "Avoirs de réserve ","elements": []}
            ]}
        ]},
        {"name": "DEBIT",
        "elements": [
            {"name": "COMPTE DES OPERATIONS FINANCIERES",
            "elements": [
                {"name": "Investissements directs",
                "elements": [
                    {"name": "A l'étranger", "elements": []},
                    {"name": "Dans l' économie nationale", "elements": []}
                ]},
                {"name": "Investissements de portefeuille",
                "elements": [
                    {"name": "Avoirs", "elements": []},
                    {"name": "Engagements", "elements": []}
                ]},
                {"name": "Autres investissements ",
                "elements": [
                    {"name": "Crédits commerciaux",
                    "elements": [
                        {"name": "Autres secteurs", "elements": []}
                    ]},
                    {"name": "Prêts",
                    "elements":[
                        {"name": "Administrations", "elements": []},
                        {"name": "Banques", "elements": []},
                        {"name": "Autres secteurs", "elements": []}
                    ]},
                    {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                    {"name": "Autres", "elements": []}
                ]},
                {"name": "Avoirs de réserve ", "elements": []}
            ]}
        ]}
    ]
    return BP_A_MBP5_hierarchy


#####################################################################################################################
##################################BP_A_MBP5##########################################################################
@api.get('/BP_A_MBP5/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1, "Balance de paiement": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "valeur": 1}));
    else:
        a = list(BP_A_MBP5.find({}, {"_id": 0, "Date": 1, "Balance de paiement": 1, "Cat�gorie": 1,
                                     "Nature de l'op�ration": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

#######################################################################################################################################################"
########################################################BP_A_MBP6_hierarchy####################################################################################
###############################################################################################################################################"############

@api.get("/BP_A_MBP6/")
async def hierarchy():
    BP_A_MBP6_hierarchy=[

        {"name":"SOLDE",
        "elements":[
            {"name":"COMPTE DES TRANSACTIONS COURANTES",
             "elements": [
                 {"name": "BIENS", "elements": []},
                 {"name": "SERVICES", "elements": []},
                 {"name": "REVENU PRIMAIRE", "elements": []},
                 {"name": "REVENU SECONDAIRE", "elements": []},
                 {"name": "INVESTISSEMENTS DIRECTS", "elements": []},
                 {"name": "INVESTISSEMENTS DE PORTEFEUILLE", "elements": []},
                 {"name": "DÉRIVÉS FINANCIERS", "elements": []},
                 {"name": "AUTRES INVESTISSEMENTS", "elements": []},
                 {"name": "AVOIRS DE RÉSERVE", "elements": []}
                ]
            }
        ]},
        {"name": "CREDIT",
        "elements": [
            {"name": "COMPTE DES TRANSACTIONS COURANTES",
            "elements": [
                {"name": "BIENS ET SERVICES",
                 "elements": [
                     {"name": "BIENS",
                      "elements": [
                          {"name": "Marchandises générales", "elements": []},
                          {"name": "Exportations nettes du négoce", "elements": []},
                          {"name": "Or non monétaire", "elements": []}

                      ]
                      },
                     {"name": "SERVICES",
                      "elements": [
                            {"name": "Services de fabrication fournis sur des intrants physiques détenus par des tiers","elements": []},
                            {"name": "Services d’entretien et de réparation n.i.a.","elements": []},
                            {"name": "Transports",
                            "elements": [
                               {"name": "Transports maritimes", "elements": []},
                               {"name": "Transports aériens", "elements": []},
                               {"name": "Autres transports", "elements": []},
                               {"name": "Services postaux et de messagerie", "elements": []}
                            ]
                            },
                          {"name": "Voyages",
                           "elements": [
                               {"name": "Voyages à titre professionnel", "elements": []},
                               {"name": "Voyages à titre personnel", "elements": []}
                           ]
                           },
                          {"name": "Constructions", "elements": []},
                          {"name": "Services d’assurance et de pension", "elements": []},
                          {"name": "Services financiers", "elements": []},
                          {"name": "Frais pour usage de la propriété intellectuelle n.i.a.", "elements": []},
                          {"name": "Services de télécommunications, d’informatique et d’information", "elements": []},
                          {"name": "Autres services aux entreprises", "elements": []},
                          {"name": "Services personnels, culturels et relatifs aux loisirs", "elements": []},
                          {"name": "Biens et services des administrations publiques n.i.a.", "elements": []}
                      ]},
                     {"name": "REVENU PRIMAIRE",
                      "elements": [
                          {"name": "Revenus des investissements",
                           "elements":[
                                {"name": "Investissements directs", "elements": []},
                                {"name": "Investissements de portefeuille", "elements": []},
                                {"name": "Autres investissements", "elements": []},
                                {"name": "Autres investissements", "elements": []}
                           ]
                           },
                           {"name": "Revenus des investissements","elements": []}
                      ]
                      },
                     {"name": "REVENU SECONDAIRE",
                      "elements": [
                          {"name": "Publics", "elements": []},
                          {"name": "Privés", "elements": []}
                      ]
                      }
                 ]}
            ]}
        ]},
        {"name": "DEBIT",
        "elements": [
            {"name": "COMPTE DES TRANSACTIONS COURANTES ",
            "elements": [
                {"name": "BIENS ET SERVICES",
                 "elements": [
                     {"name": "BIENS",
                      "elements": [
                          {"name": "Marchandises générales", "elements": []},
                          {"name": "Exportations nettes du négoce", "elements": []},
                          {"name": "Or non monétaire", "elements": []}
                      ]
                      },
                     {"name": "SERVICES",
                      "elements": [
                          {"name": "Services de fabrication fournis sur des intrants physiques détenus par des tiers","elements": []},
                          {"name": "Services d’entretien et de réparation n.i.a.","elements": []},
                          {"name": "Transports",
                           "elements": [
                               {"name": "Transports maritimes", "elements": []},
                               {"name": "Transports aériens", "elements": []},
                               {"name": "Autres transports", "elements": []},
                               {"name": "Services postaux et de messagerie", "elements": []}
                           ]
                           },
                          {"name": "Voyages",
                           "elements": [
                               {"name": "Voyages à titre professionnel", "elements": []},
                               {"name": "Voyages à titre personnel", "elements": []}
                           ]},
                          {"name": "Constructions", "elements": []},
                          {"name": "Services d’assurance et de pension", "elements": []},
                          {"name": "Services financiers", "elements": []},
                          {"name": "Frais pour usage de la propriété intellectuelle n.i.a.", "elements": []},
                          {"name": "Services de télécommunications, d’informatique et d’information", "elements": []},
                          {"name": "Autres services aux entreprises", "elements": []},
                          {"name": "Services personnels, culturels et relatifs aux loisirs", "elements": []},
                          {"name": "Biens et services des administrations publiques n.i.a.", "elements": []}

                      ]},
                     {"name": "REVENU PRIMAIRE",
                      "elements": [
                          {"name": "Revenus des investissements",
                           "elements": [
                               {"name": "Investissements directs", "elements": []},
                               {"name": "Investissements de portefeuille", "elements": []},
                               {"name": "Autres investissements", "elements": []},
                               {"name": "Avoirs de réserve", "elements": []}

                           ]
                           },
                          {"name": "Autres revenus primaires", "elements": []}
                      ]
                      },
                     {"name": "REVENU SECONDAIRE",
                      "elements": [
                          {"name": "Publics", "elements": []},
                          {"name": "Privés", "elements": []}
                      ]
                      }
                 ]}
            ]}
        ]},
        {"name": "ACQUISITION NETTE D'AVOIRS",
        "elements":[
            {"name":"COMPTE FINANCIER",
            "elements":[
                {"name": "Investissements directs",
                "elements": [
                    {"name": "Actions et parts de fonds de placement", "elements": []},
                    {"name": "Instruments de dette", "elements": []}
                ]
                },
                {"name": "Investissements de portefeuille",
                 "elements": [
                    {"name": "Actions et parts de fonds de placement", "elements": []},
                    {"name": "Titres de créance", "elements": []}
                ]
                },
                {"name": "DÉRIVÉS FINANCIERS","elements": []},
                {"name": "Autres investissements",
                "elements": [
                    {"name": "Autres participations","elements": []},
                    {"name": "Numéraire et dépôts", "elements": []},
                    {"name": "Prêts", "elements": []},
                    {"name": "Systèmes d'assurances, de pensions et de garanties standard", "elements": []},
                    {"name": "Crédits commerciaux et avances", "elements": []},
                    {"name": "Autres comptes à recevoir/à payer", "elements": []},
                ]
                },
                {"name": "AVOIRS DE RÉSERVE","elements": []}
            ]
            },
        ]},

        {"name": "ACCROISSEMENT NET DES ENGAGEMENTS",
        "elements": [
            {"name": "COMPTE FINANCIER",
            "elements": [
                {"name": "Investissements directs",
                "elements": [
                    {"name": "Actions et parts de fonds de placement", "elements": []},
                    {"name": "Instruments de dette", "elements": []}
                ]},
                {"name": "Investissements de portefeuille",
                "elements": [
                    {"name": "Actions et parts de fonds de placement", "elements": []},
                    {"name": "Titres de créance", "elements": []}
                ]},
                {"name": "DÉRIVÉS FINANCIERS","elements": []},
                {"name": "Autres investissements ",
                "elements": [
                    {"name": "Numéraire et dépôts","elements": []},
                    {"name": "Prêts", "elements": []},
                    {"name": "Systèmes d'assurances, de pensions et de garanties standard", "elements": []},
                    {"name": "Crédits commerciaux et avances", "elements": []},
                    {"name": "Autres comptes à recevoir/à payer", "elements": []}
                ]}
            ]}
        ]}
    ]
    return BP_A_MBP6_hierarchy

######################################################################################################################
##########################################BP_A_MBP6_0#################################################################
@api.get('/BP_A_MBP6_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP6_0.find({"date": {"$gte": start, "$lte": end}},
                                  {"_id": 0, "date": 1, "balance des paiements annuelle selon MBP6": 1, "cat�gorie": 1,
                                   "nature ": 1, "valeur": 1}));
    else:
        a = list(BP_A_MBP6_0.find({},
                                  {"_id": 0, "date": 1, "balance des paiements annuelle selon MBP6": 1, "cat�gorie": 1,
                                   "nature ": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


######################################################################################################################
########################################BP_T_MBP5_Hierarchy###########################################################
@api.get("/BP_T_MBP5")
async def hierarchy():
    BP_T_MBP5_hierarchy=[

        {"name":"SOLDE",
        "elements":[
            {"name":"COMPTE DES TRANSACTIONS COURANTES",
             "elements": [
                 {"name": "BIENS", "elements": []},
                 {"name": "SERVICES", "elements": []},
                 {"name": "REVENUS", "elements": []},
                 {"name": "TRANSFERTS COURANTS", "elements": []},
                 {"name": "INVESTISSEMENTS DIRECTS", "elements": []},
                 {"name": "INVESTISSEMENTS DE PORTEFEUILLE", "elements": []},
                 {"name": "AUTRES INVESTISSEMENTS", "elements": []},
                 {"name": "AVOIRS DE RÉSERVE", "elements": []}
                ]
            }
        ]},
        {"name": "CREDIT",
        "elements": [
            {"name": "COMPTE DES TRANSACTIONS COURANTES",
            "elements": [
                {"name": "BIENS",
                "elements": [
                    {"name" : "Marchandises générales", "elements": []},
                    {"name" : "Biens importés sans paiement et réexportés après transformation", "elements": []},
                    {"name" : "Achats de biens dans les ports", "elements": []},
                    ]
                },
                {"name": "SERVICES",
                "elements": [
                    {"name": "Transports",
                    "elements": [
                        {"name": "Transports maritimes", "elements": []},
                        {"name": "Transports aériens", "elements": []},
                        {"name": "Autres transports", "elements": []},
                        ]
                    },
                    {"name": "Voyages",
                    "elements": [
                        {"name": "Voyages à titre professionnel", "elements": []},
                        {"name": "Voyages à titre personnel", "elements": []}
                        ]
                    },
                    {"name": "Services de communication", "elements": []},
                    {"name": "Services d'assurance", "elements": []},
                    {"name": "Redevances et droits de licence", "elements": []},
                    {"name": "Autres services aux entreprises", "elements": []},
                    {"name": "Services fournis ou reçus par les administrations publiques N.C.A", "elements": []}
                ]},
                {"name": "REVENUS",
                "elements": [
                    {"name": "Administrations", "elements": []},
                    {"name": "Autorités monétaires", "elements": []},
                    {"name": "Banques", "elements": []},
                    {"name": "Autres secteurs", "elements": []},
                    ]
                },
                {"name": "TRANSFERTS COURANTS",
                "elements": [
                    {"name": "Publics", "elements": []},
                    {"name": "Privés", "elements": []}
                    ]
                }
            ]}
        ]},
        {"name": "DEBIT",
        "elements": [
            {"name": "COMPTE DES TRANSACTIONS COURANTES ",
            "elements": [
                {"name": "BIENS",
                "elements": [
                    {"name": "Marchandises générales", "elements": []},
                    {"name": "Biens importés sans paiement et réexportés après transformation", "elements": []},
                    {"name": "Achats de biens dans les ports", "elements": []}
                    ]
                },
                {"name": "SERVICES",
                "elements": [
                    {"name": "Transports",
                    "elements": [
                        {"name": "Transports maritimes", "elements":[]},
                        {"name": "Transports aériens", "elements": []},
                        {"name": "Autres transports", "elements": []},
                        ]
                    },
                    {"name": "Voyages",
                    "elements": [
                        {"name": "Voyages à titre professionnel", "elements":[]},
                        {"name": "Voyages à titre personnel", "elements":[]},
                    ]},
                    {"name": "Services de communication", "elements": []},
                    {"name": "Services d'assurance", "elements": []},
                    {"name": "Redevances et droits de licence", "elements": []},
                    {"name": "Autres services aux entreprises", "elements": []},
                    {"name": "Services fournis ou reçus par les administrations publiques N.C.A", "elements": []}
                ]},
                {"name": "REVENUS",
                "elements": [
                    {"name": "Administrations", "elements": []},
                    {"name": "Autorités monétaires", "elements": []},
                    {"name": "Banques", "elements": []},
                    {"name": "Autres secteurs", "elements": []},
                    ]
                },
                {"name": "TRANSFERTS COURANTS",
                "elements": [
                    {"name": "Publics", "elements": []},
                    {"name": "Privés", "elements": []}
                    ]
                }
            ]}
        ]},
        {"name": "CREDIT",
        "elements":[
            {"name":"COMPTE DES OPERATIONS FINANCIERES",
            "elements":[
                {"name": "Investissements directs",
                "elements": [
                    {"name": "A l'étranger", "elements": []},
                    {"name": "Dans l' économie nationale", "elements": []}
                    ]
                },
                {"name": "Investissements de portefeuille", "elements": [
                    {"name": "Avoirs", "elements": []},
                    {"name": "Engagements", "elements": []}
                    ]
                },
                {"name": "Autres investissements",
                "elements": [
                    {"name": "Crédits commerciaux",
                    "elements": [
                        {"name": "Autres secteurs", "elements": []}
                    ]},
                    {"name": "Prêts",
                    "elements": [
                        {"name": "Administrations","elements": []},
                        {"name": "Banques","elements": []},
                        {"name": "Autres secteurs","elements": []},
                    ]},
                    {"name": "Monnaie fiduciaire et dépôts","elements": []},
                    {"name": "Autres OF","elements": []},
                ]},
                {"name": "Avoirs de réserve ","elements": []}
            ]}
        ]},
        {"name": "DEBIT",
        "elements": [
            {"name": "COMPTE DES OPERATIONS FINANCIERES",
            "elements": [
                {"name": "Investissements directs",
                "elements": [
                    {"name": "A l'étranger", "elements": []},
                    {"name": "Dans l' économie nationale", "elements": []}
                ]},
                {"name": "Investissements de portefeuille",
                "elements": [
                    {"name": "Avoirs", "elements": []},
                    {"name": "Engagements", "elements": []}
                ]},
                {"name": "Autres investissements ",
                "elements": [
                    {"name": "Crédits commerciaux",
                    "elements": [
                        {"name": "Autres secteurs", "elements": []}
                    ]},
                    {"name": "Prêts",
                    "elements":[
                        {"name": "Administrations", "elements": []},
                        {"name": "Banques", "elements": []},
                        {"name": "Autres secteurs", "elements": []}
                    ]},
                    {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                    {"name": "Autres OF", "elements": []}
                ]},
                {"name": "Avoirs de réserve ", "elements": []}
            ]}
        ]}
    ]
    return BP_T_MBP5_hierarchy
######################################################################################################################
###################################################BP_T_MBP5##########################################################
@api.get('/BP_T_MBP5/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_T_MBP5.find({"date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "date": 1, "periode": 1, "Balance des paiements trimestrielle selon MBP5": 1,
                                 "cat�gorie": 1, "nature ": 1, "valeur": 1}));
    else:
        a = list(BP_T_MBP5.find({},
                                {"_id": 0, "date": 1, "periode": 1, "Balance des paiements trimestrielle selon MBP5": 1,
                                 "cat�gorie": 1, "nature ": 1, "valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#######################################################################################################################
###########################################BP_T_MBP6_hierarchy#########################################################
#######################################################################################################################
@api.get("/BP_T_MBP6/")
async def hierarchy():
    BP_T_MBP6_hierarchy=[

        {"name":"SOLDE",
        "elements":[
            {"name":"COMPTE DES TRANSACTIONS COURANTES",
             "elements": [
                 {"name": "BIENS", "elements": []},
                 {"name": "SERVICES", "elements": []},
                 {"name": "REVENU PRIMAIRE", "elements": []},
                 {"name": "REVENU SECONDAIRE", "elements": []},
                 {"name": "INVESTISSEMENTS DIRECTS", "elements": []},
                 {"name": "INVESTISSEMENTS DE PORTEFEUILLE", "elements": []},
                 {"name": "DÉRIVÉS FINANCIERS", "elements": []},
                 {"name": "AUTRES INVESTISSEMENTS", "elements": []},
                 {"name": "AVOIRS DE RÉSERVE", "elements": []}
                ]
            }
        ]},
        {"name": "CREDIT",
        "elements": [
            {"name": "COMPTE DES TRANSACTIONS COURANTES",
            "elements": [
                {"name": "BIENS ET SERVICES",
                 "elements": [
                     {"name": "BIENS",
                      "elements": [
                          {"name": "Marchandises générales", "elements": []},
                          {"name": "Exportations nettes du négoce", "elements": []},
                          {"name": "Or non monétaire", "elements": []}

                      ]
                      },
                     {"name": "SERVICES",
                      "elements": [
                            {"name": "Services de fabrication fournis sur des intrants physiques détenus par des tiers","elements": []},
                            {"name": "Services d’entretien et de réparation n.i.a.","elements": []},
                            {"name": "Transports",
                            "elements": [
                               {"name": "Transports maritimes", "elements": []},
                               {"name": "Transports aériens", "elements": []},
                               {"name": "Autres transports", "elements": []},
                               {"name": "Services postaux et de messagerie", "elements": []}
                            ]
                            },
                          {"name": "Voyages",
                           "elements": [
                               {"name": "Voyages à titre professionnel", "elements": []},
                               {"name": "Voyages à titre personnel", "elements": []}
                           ]
                           },
                          {"name": "Constructions", "elements": []},
                          {"name": "Services d’assurance et de pension", "elements": []},
                          {"name": "Services financiers", "elements": []},
                          {"name": "Frais pour usage de la propriété intellectuelle n.i.a.", "elements": []},
                          {"name": "Services de télécommunications, d’informatique et d’information", "elements": []},
                          {"name": "Autres services aux entreprises", "elements": []},
                          {"name": "Services personnels, culturels et relatifs aux loisirs", "elements": []},
                          {"name": "Biens et services des administrations publiques n.i.a.", "elements": []}
                      ]},
                     {"name": "REVENU PRIMAIRE",
                      "elements": [
                          {"name": "Revenus des investissements",
                           "elements":[
                                {"name": "Investissements directs", "elements": []},
                                {"name": "Investissements de portefeuille", "elements": []},
                                {"name": "Autres investissements", "elements": []},
                                {"name": "Autres investissements", "elements": []}
                           ]
                           },
                           {"name": "Revenus des investissements","elements": []}
                      ]
                      },
                     {"name": "REVENU SECONDAIRE",
                      "elements": [
                          {"name": "Publics", "elements": []},
                          {"name": "Privés", "elements": []}
                      ]
                      }
                 ]}
            ]}
        ]},
        {"name": "DEBIT",
        "elements": [
            {"name": "COMPTE DES TRANSACTIONS COURANTES ",
            "elements": [
                {"name": "BIENS ET SERVICES",
                 "elements": [
                     {"name": "BIENS",
                      "elements": [
                          {"name": "Marchandises générales", "elements": []},
                          {"name": "Exportations nettes du négoce", "elements": []},
                          {"name": "Or non monétaire", "elements": []}
                      ]
                      },
                     {"name": "SERVICES",
                      "elements": [
                          {"name": "Services de fabrication fournis sur des intrants physiques détenus par des tiers","elements": []},
                          {"name": "Services d’entretien et de réparation n.i.a.","elements": []},
                          {"name": "Transports",
                           "elements": [
                               {"name": "Transports maritimes", "elements": []},
                               {"name": "Transports aériens", "elements": []},
                               {"name": "Autres transports", "elements": []},
                               {"name": "Services postaux et de messagerie", "elements": []}
                           ]
                           },
                          {"name": "Voyages",
                           "elements": [
                               {"name": "Voyages à titre professionnel", "elements": []},
                               {"name": "Voyages à titre personnel", "elements": []}
                           ]},
                          {"name": "Constructions", "elements": []},
                          {"name": "Services d’assurance et de pension", "elements": []},
                          {"name": "Services financiers", "elements": []},
                          {"name": "Frais pour usage de la propriété intellectuelle n.i.a.", "elements": []},
                          {"name": "Services de télécommunications, d’informatique et d’information", "elements": []},
                          {"name": "Autres services aux entreprises", "elements": []},
                          {"name": "Services personnels, culturels et relatifs aux loisirs", "elements": []},
                          {"name": "Biens et services des administrations publiques n.i.a.", "elements": []}

                      ]},
                     {"name": "REVENU PRIMAIRE",
                      "elements": [
                          {"name": "Revenus des investissements",
                           "elements": [
                               {"name": "Investissements directs", "elements": []},
                               {"name": "Investissements de portefeuille", "elements": []},
                               {"name": "Autres investissements", "elements": []},
                               {"name": "Avoirs de réserve", "elements": []}

                           ]
                           },
                          {"name": "Autres revenus primaires", "elements": []}
                      ]
                      },
                     {"name": "REVENU SECONDAIRE",
                      "elements": [
                          {"name": "Publics", "elements": []},
                          {"name": "Privés", "elements": []}
                      ]
                      }
                 ]}
            ]}
        ]},
        {"name": "ACQUISITION NETTE D'AVOIRS",
        "elements":[
            {"name":"COMPTE FINANCIER",
            "elements":[
                {"name": "Investissements directs",
                "elements": [
                    {"name": "Actions et parts de fonds de placement", "elements": []},
                    {"name": "Instruments de dette", "elements": []}
                ]
                },
                {"name": "Investissements de portefeuille",
                 "elements": [
                    {"name": "Actions et parts de fonds de placement", "elements": []},
                    {"name": "Titres de créance", "elements": []}
                ]
                },
                {"name": "DÉRIVÉS FINANCIERS","elements": []},
                {"name": "Autres investissements",
                "elements": [
                    {"name": "Autres participations","elements": []},
                    {"name": "Numéraire et dépôts", "elements": []},
                    {"name": "Prêts", "elements": []},
                    {"name": "Systèmes d'assurances, de pensions et de garanties standard", "elements": []},
                    {"name": "Crédits commerciaux et avances", "elements": []},

                ]
                },
                {"name": "AVOIRS DE RÉSERVE","elements": []}
            ]
            },
        ]},

        {"name": "ACCROISSEMENT NET DES ENGAGEMENTS",
        "elements": [
            {"name": "COMPTE FINANCIER",
            "elements": [
                {"name": "Investissements directs",
                "elements": [
                    {"name": "Actions et parts de fonds de placement", "elements": []},
                    {"name": "Instruments de dette", "elements": []}
                ]},
                {"name": "Investissements de portefeuille",
                "elements": [
                    {"name": "Actions et parts de fonds de placement", "elements": []},
                    {"name": "Titres de créance", "elements": []}
                ]},
                {"name": "DÉRIVÉS FINANCIERS","elements": []},
                {"name": "Autres investissements ",
                "elements": [
                    {"name": "Autres participations", "elements": []},
                    {"name": "Numéraire et dépôts","elements": []},
                    {"name": "Prêts", "elements": []},
                    {"name": "Systèmes d'assurances, de pensions et de garanties standard", "elements": []},
                    {"name": "Crédits commerciaux et avances", "elements": []},

                ]}
            ]}
        ]}
    ]
    return BP_T_MBP6_hierarchy
#######################################################################################################################
##################################################BP_T_MBP6_3##########################################################
@api.get('/BP_T_MBP6_3/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_T_MBP6_3.find({"Date": {"$gte": start, "$lte": end}},
                                  {"_id": 0, "Date": 1, "P�riode": 1, "Balance des paiements": 1, "Cat�gorie": 1,
                                   "Nature d'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_T_MBP6_3.find({}, {"_id": 0, "Date": 1, "P�riode": 1, "Balance des paiements": 1, "Cat�gorie": 1,
                                       "Nature d'op�ration": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
