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
db2 = client['HCP']
db3 = client['Tourisme']
db4 = client['MEF']
db5 = client ['Enseignement']
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

BP_A_MBP5_CTC_solde = db.BP_A_MBP5_CTC_solde
BP_A_MBP5_CTC_credit = db.BP_A_MBP5_CTC_credit
BP_A_MBP5_CTC_debit = db.BP_A_MBP5_CTC_debit
BP_A_MBP5_COF_credit = db.BP_A_MBP5_COF_credit
BP_A_MBP5_COF_debit = db.BP_A_MBP5_COF_debit

BP_T_MBP5_CTC_SOLDE = db.BP_T_MBP5_CTC_SOLDE
BP_T_MBP5_CTC_CREDIT = db.BP_T_MBP5_CTC_CREDIT
BP_T_MBP5_CTC_DEBIT = db.BP_T_MBP5_CTC_DEBIT
BP_T_MBP5_COF_CREDIT = db.BP_T_MBP5_COF_CREDIT
BP_T_MBP5_COF_DEBIT = db.BP_T_MBP5_COF_DEBIT

BP_A_MBP6_CTC_SOLDE= db.BP_A_MBP6_CTC_SOLDE
BP_A_MBP6_CTC_CREDIT = db.BP_A_MBP6_CTC_CREDIT
BP_A_MBP6_CTC_DEBIT = db.BP_A_MBP6_CTC_DEBIT
BP_A_MBP6_CF_ANA = db.BP_A_MBP6_CF_ANA
BP_A_MBP6_CF_ANE = db.BP_A_MBP6_CF_ANE

BP_T_MBP6_CTC_SOLDE= db.BP_T_MBP6_CTC_SOLDE
BP_T_MBP6_CTC_CREDIT = db.BP_T_MBP6_CTC_CREDIT
BP_T_MBP6_CTC_DEBIT = db.BP_T_MBP6_CTC_DEBIT
BP_T_MBP6_CF_ANA = db.BP_T_MBP6_CF_ANA
BP_T_MBP6_CF_ANE = db.BP_T_MBP6_CF_ANE

Arrivees_touristiques	= db3.Arrivees_touristiques
Recettes_en_devises  = db3.Recettes_en_devises
arrivees_touristiques_par_nat = db3.arrivees_touristiques_par_nat

IPC_2006 = db2.IPC_2006
IPC_2017 = db2.IPC_2017

DETTE_EXTERIEURE_PUBLIQUE = db4.DETTE_EXTERIEURE_PUBLIQUE
DETTE_DU_TRESOR_SERVICE_DE_LA_DETTE = db4.DETTE_DU_TRESOR_SERVICE_DE_LA_DETTE
DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE = db4.DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE
DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL = db4.DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL
DETTE_DU_TRESOR_CHARGES_EN_INTERETS = db4.DETTE_DU_TRESOR_CHARGES_EN_INTERETS
dette_des_etab_et_Eses_Services_DE_LA_DETTE = db4.dette_des_etab_et_Eses_Services_DE_LA_DETTE
dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE = db4.dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE 
dette_des_etab_et_Eses_charges_en_principal = db4.dette_des_etab_et_Eses_charges_en_principal
Dette_des_etab_et_Eses_charges_en_interet = db4.Dette_des_etab_et_Eses_charges_en_interet

dette_brute_sec_bancaire = db4.dette_brute_sec_bancaire
dette_brute_inves_directs = db4.dette_brute_inves_directs
dette_brute_autres_sec = db4.dette_brute_autres_sec
dette_brute_autorites_mon = db4.dette_brute_autorites_mon
dette_brute_administration = db4.dette_brute_administration

PIB_approche_revenu = db2.PIB_approche_revenu
PIB_prix_constants = db2.PIB_prix_constants
PIB_prix_courants = db2.PIB_prix_courants

Production_d_agrumes = db2.Production_d_agrumes
Production_d_oeufs = db2.Production_d_oeufs
Production_de_bois_d_oeuvre = db2.Production_de_bois_d_oeuvre
Production_de_bois_de_feu = db2.Production_de_bois_de_feu
Production_de_bois_industriel = db2.Production_de_bois_industriel
Production_de_la_viande_blanche = db2.Production_de_la_viande_blanche
Production_de_legumineuses = db2.Production_de_legumineuses
Superficie_cultivee_des_cultures_fourrageres = db2.Superficie_cultivee_des_cultures_fourrageres
Superficie_laissee_en_jachere = db2.Superficie_laissee_en_jachere
superficie_cultivee_des_cereales = db2.superficie_cultivee_des_cereales

NB_DE_CLASSES = db5.NB_DE_CLASSES
ELEVES_DES_ECOLES_CORANIQUES = db5.ELEVES_DES_ECOLES_CORANIQUES
Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public = db5.Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public
NB_DE_CLASSES_EC = db5.NB_DE_CLASSES_EC
Nombre_classe_enseignement_primaire_public = db5.Nombre_classe_enseignement_primaire_public
Nombre_de_classe_du_secondaire_collegial = db5.Nombre_de_classe_du_secondaire_collegial
Nombre_de_classes_de_enseignement_secondaire_qualifiant_public = db5.Nombre_de_classes_de_enseignement_secondaire_qualifiant_public
Nombre_de_colleges_annexes_du_secondaire_collegial = db5.Nombre_de_colleges_annexes_du_secondaire_collegial
Nombre_de_colleges_du_secondaire_collegial = db5.Nombre_de_colleges_du_secondaire_collegial
Nombre_de_salles_utilisees_du_secondaire_collegial = db5.Nombre_de_salles_utilisees_du_secondaire_collegial
Nombre_ecoles_autonomes_primaire = db5.Nombre_ecoles_autonomes_primaire
Nombre_eleve_enseignement_secondaire_qualifiant_prive = db5.Nombre_eleve_enseignement_secondaire_qualifiant_prive
Nombre_eleve_enseignement_secondaire_qualifiant_public = db5.Nombre_eleve_enseignement_secondaire_qualifiant_public
Nombre_eleves_dans_enseignement_primaire_public = db5.Nombre_eleves_dans_enseignement_primaire_public
Nombre_eleves_doublant_dans_enseignement_primaire_public = db5.Nombre_eleves_doublant_dans_enseignement_primaire_public
Nombre_eleves_doublant_du_secondaire_collegial = db5.Nombre_eleves_doublant_du_secondaire_collegial
Nombre_eleves_du_secondaire_collegial = db5.Nombre_eleves_du_secondaire_collegial
Nombre_eleves_enseignement_primaire_prive = db5.Nombre_eleves_enseignement_primaire_prive
Nombre_eleves_enseignement_primaire_public = db5.Nombre_eleves_enseignement_primaire_public
Nombre_eleves_enseignement_secondaire_collegial_prive = db5.Nombre_eleves_enseignement_secondaire_collegial_prive
Nombre_enseignant_du_secondaire_collegial_prive = db5.Nombre_enseignant_du_secondaire_collegial_prive
Nombre_etablissements_enseignement_primaire_prive = db5.Nombre_etablissements_enseignement_primaire_prive
Nombre_etablissements_primaire = db5.Nombre_etablissements_primaire
Nombre_formateurs_dans_les_centres_de_formation_professionnelle = db5.Nombre_formateurs_dans_les_centres_de_formation_professionnelle
Nombre_laureats_centres_formation_professionnelle = db5.Nombre_laureats_centres_formation_professionnelle
Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public = db5.Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public
Nombre_lycees_enseignement_secondaire_qualifiant_public = db5.Nombre_lycees_enseignement_secondaire_qualifiant_public
Nombre_salles_enseignement_secondaire_qualifiant_prive = db5.Nombre_salles_enseignement_secondaire_qualifiant_prive
Nombre_salles_utilisees_enseignement_primaire_prive = db5.Nombre_salles_utilisees_enseignement_primaire_prive
Nombre_salles_utilisees_enseignement_primaire_public = db5.Nombre_salles_utilisees_enseignement_primaire_public
Nombre_salles_utilisees_enseignement_secondaire_qualifiant = db5.Nombre_salles_utilisees_enseignement_secondaire_qualifiant
Nombre_satellites_primaire = db5.Nombre_satellites_primaire
Nombre_secteurs_scolaires_primaire = db5.Nombre_secteurs_scolaires_primaire
Personnel_enseignant_de_enseignement_primaire_prive = db5.Personnel_enseignant_de_enseignement_primaire_prive
Personnel_enseignant_de_enseignement_secondaire_collegial_public = db5.Personnel_enseignant_de_enseignement_secondaire_collegial_public
Personnel_enseignant_enseignement_primaire_public = db5.Personnel_enseignant_enseignement_primaire_public
Personnel_enseignant_enseignement_secondaire_qualifiant_prive = db5.Personnel_enseignant_enseignement_secondaire_qualifiant_prive
Personnel_enseignant_enseignement_secondaire_qualifiant_public = db5.Personnel_enseignant_enseignement_secondaire_qualifiant_public
Personnel_enseignant_enseignement_secondaire_qualifiant_public_2 = db5.Personnel_enseignant_enseignement_secondaire_qualifiant_public_2
effectif_etablissement_secondaire_collegial_prive = db5.effectif_etablissement_secondaire_collegial_prive
effectif_etablissement_secondaire_qualifiant_prive = db5.effectif_etablissement_secondaire_qualifiant_prive
eleves_doublant_de_enseignement_secondaire_qualifiant_public = db5.eleves_doublant_de_enseignement_secondaire_qualifiant_public

Taux_d_achevement= db5.Taux_d_achevement
Budget_education_national = db5.Budget_education_national
Nombre_d_etablissements_EC= db5.Nombre_d_etablissements_EC
Personnel_enseignant_EC= db5.Personnel_enseignant_EC




Approvisionnement_energetique_total = db2.Approvisionnement_energetique_total
Consommation_energie = db2.Consommation_energie
Consommation_de_produits_petroliers = db2.Consommation_de_produits_petroliers
Consommation_de_produits_petroliers_energetiques = db2.Consommation_de_produits_petroliers_energetiques
Consommation_de_produits_petroliers_non_energetiques = db2.Consommation_de_produits_petroliers_non_energetiques
Consommation_des_huiles_et_graisses = db2.Consommation_des_huiles_et_graisses
Consommation_par_les_industriels_autoproducteurs = db2.Consommation_par_les_industriels_autoproducteurs
Consommation_par_les_petites_distributions_isolees = db2.Consommation_par_les_petites_distributions_isolees
Exportation_de_charbon = db2.Exportation_de_charbon
Exportation_de_Naphta = db2.Exportation_de_Naphta
Exportation_des_produits_petroliers = db2.Exportation_des_produits_petroliers
Longueur_des_lignes_de_transport_electricite_haute_tension = db2.Longueur_des_lignes_de_transport_electricite_haute_tension
Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc = db2.Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc
Personnel_de_ONE = db2.Personnel_de_ONE
Production_concessionnelle = db2.Production_concessionnelle
Production_des_apports_des_tiers = db2.Production_des_apports_des_tiers
Production_du_parc_eolien_de_ONE = db2.Production_du_parc_eolien_de_ONE
Production_nette_de_charbon = db2.Production_nette_de_charbon
Production_nette_electricite = db2.Production_nette_electricite
Production_nette_des_petites_distributions_isolees = db2.Production_nette_des_petites_distributions_isolees
Production_total_de_ONE = db2.Production_total_de_ONE
Puissance_installee_par_ONE = db2.Puissance_installee_par_ONE
Puissance_totale_installee_au_maroc = db2.Puissance_totale_installee_au_maroc
Ventes_locales_de_charbon = db2.Ventes_locales_de_charbon


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
#######################################################################################################################""
#######################################Comext_import_hierarchy####################################
########################################################################################################################

@api.get("/Comext_import/")
async def hierarchy():
    Comext_import_hierarchy=[

        {"name": "Type",
         "elements": [

             {"name": "ALIMENTATION. BOISSON ET TABAC CVS-CJO", "elements": []},
             {"name": "ENERGIE ET LUBRIFIANTS CVS-CJO", "elements": []},
             {"name": "PRODUITS BRUTS D'ORIGINE ANIMALE ET VEGETALE CVS-CJO", "elements": []},
             {"name": "PRODUITS BRUTS D'ORIGINE MINERALE CVS-CJO", "elements": []},
             {"name": "DEMI PRODUITS CVS-CJO", "elements": []},
             {"name": "PRODUITS FINIS D'EQUIPEMENT CVS-CJO", "elements": []},
             {"name": "PRODUITS FINIS DE CONSOMMATION CVS-CJO", "elements": []}
         ]},

    ]
    return Comext_import_hierarchy


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
#######################################################################################################################""
#######################################Comext_Export_hierarchy####################################
########################################################################################################################

@api.get("/Comext_Export/")
async def hierarchy():
    Comext_Export_hierarchy=[

        {"name": "Type",
         "elements": [

             {"name": "ALIMENTATION. BOISSON ET TABAC CVS-CJO", "elements": []},
             {"name": "ENERGIE ET LUBRIFIANTS CVS-CJO", "elements": []},
             {"name": "PRODUITS BRUTS D'ORIGINE ANIMALE ET VEGETALE CVS-CJO", "elements": []},
             {"name": "PRODUITS BRUTS D'ORIGINE MINERALE CVS-CJO", "elements": []},
             {"name": "DEMI PRODUITS CVS-CJO", "elements": []},
             {"name": "PRODUITS FINIS D'EQUIPEMENT CVS-CJO", "elements": []},
             {"name": "PRODUITS FINIS DE CONSOMMATION CVS-CJO", "elements": []}
         ]},

    ]
    return Comext_Export_hierarchy
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
#######################################################################################################################""
#######################################Comext_TOTAL_hierarchy####################################
########################################################################################################################

@api.get("/Comext_TOTAL/")
async def hierarchy():
    Comext_TOTAL_hierarchy=[

        {"name": "données commerce exterieur",
         "elements": [

             {"name": "Total Export CVS-CJO", "elements": []},
             {"name": "Total Import CVS-CJO", "elements": []}


         ]},

    ]
    return Comext_TOTAL_hierarchy


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

        {"name": "Recette MRE","elements": []}
        ]},
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
#######################################################################################################################""
#######################################IDE_Maroc_flux_Flux_nets_par_pays_hierarchy####################################
########################################################################################################################

@api.get("/IDE_Maroc_flux_Flux_nets_par_pays/")
async def hierarchy():
    IDE_Maroc_flux_Flux_nets_par_pays_hierarchy=[

        {"name": "PAYS/ORGANISMES FINANCIERS",
         "elements": [

             {"name": "France", "elements": []},
             {"name": "Espagne", "elements": []},
             {"name": "Emirats Arabes Unis", "elements": []},
             {"name": "Grande Bretagne", "elements": []},
             {"name": "Luxembourg", "elements": []},
             {"name": "Qatar", "elements": []},
             {"name": "Afrique du Sud", "elements": []},
             {"name": "Maurice", "elements": []},
             {"name": "Allemagne", "elements": []},
             {"name": "Irlande", "elements": []},
             {"name": "Suisse", "elements": []},
             {"name": "Etats-Unis", "elements": []},
             {"name": "Malte", "elements": []},
             {"name": "Chine", "elements": []},
             {"name": "Italie", "elements": []},
             {"name": "Arabie Saoudite", "elements": []},
             {"name": "Turquie", "elements": []},
             {"name": "Fonds Arabe de Développement Economique et Social", "elements": []},
             {"name": "Singapour", "elements": []},
             {"name": "Canada", "elements": []},
             {"name": "Belgique", "elements": []},
             {"name": "Suède", "elements": []},
             {"name": "Chypre", "elements": []},
             {"name": "Tunisie", "elements": []},
             {"name": "Oman", "elements": []},
             {"name": "Koweït", "elements": []},
             {"name": "Malaisie", "elements": []},
             {"name": "Portugal", "elements": []},
             {"name": "République de Corée", "elements": []},
             {"name": "Monaco", "elements": []},
             {"name": "Roumanie", "elements": []},
             {"name": "Jersey", "elements": []},
             {"name": "Russie", "elements": []},
             {"name": "Grèce", "elements": []},
             {"name": "Hong-Kong", "elements": []},
             {"name": "Liban", "elements": []},
             {"name": "Danemark", "elements": []},
             {"name": "Autriche", "elements": []},
             {"name": "Pologne", "elements": []},
             {"name": "Japon", "elements": []},
             {"name": "Islande", "elements": []},
             {"name": "Slovaquie", "elements": []},
             {"name": "Kenya", "elements": []},
             {"name": "Banque Islamique de Développement", "elements": []},
             {"name": "Bahamas", "elements": []},
             {"name": "Banque Africaine de Développement", "elements": []},
             {"name": "Cameroun", "elements": []},
             {"name": "Gabon", "elements": []},
             {"name": "Sénégal", "elements": []},
             {"name": "Congo", "elements": []},
             {"name": "Egypte", "elements": []},
             {"name": "Côte d'Ivoire", "elements": []},
             {"name": "Inde", "elements": []},
             {"name": "Jordanie", "elements": []},
             {"name": "Martinique", "elements": []},
             {"name": "Bahreïn", "elements": []},
             {"name": "Pays Bas", "elements": []},
             {"name": "Autres pays", "elements": []}

         ]},

    ]
    return IDE_Maroc_flux_Flux_nets_par_pays_hierarchy


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
    #######################################################################################################################""
    #######################################IDE_Maroc_Stock_Par_secteurs_hierarchy####################################
    ########################################################################################################################

@api.get("/IDE_Maroc_Stock_Par_secteurs/")
async def hierarchy():
        IDE_Maroc_Stock_Par_secteurs_hierarchy = [

            {"name": "SECTEURS",
             "elements": [

                 {"name": "Industrie", "elements": []},
                 {"name": "Immobilier", "elements": []},
                 {"name": "Télécommunications", "elements": []},
                 {"name": "Tourisme", "elements": []},
                 {"name": "Energie et Mines", "elements": []},
                 {"name": "Banques", "elements": []},
                 {"name": "Commerce", "elements": []},
                 {"name": "Grands Travaux", "elements": []},
                 {"name": "Holding", "elements": []},
                 {"name": "Transport", "elements": []},
                 {"name": "Assurances", "elements": []},
                 {"name": "Cimenteries", "elements": []},
                 {"name": "Agriculture", "elements": []},
                 {"name": "Pêche", "elements": []},
                 {"name": "Etudes", "elements": []},
                 {"name": "Autres services", "elements": []},
                 {"name": "Divers secteurs", "elements": []},

             ]},

        ]
        return IDE_Maroc_Stock_Par_secteurs_hierarchy


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
#######################################################################################################################""
#######################################IDE_Maroc_Stock_Par_Pays_hierarchy####################################
########################################################################################################################

@api.get("/IDE_Maroc_Stock_Par_Pays/")
async def hierarchy():
    IDE_Maroc_Stock_Par_Pays_hierarchy=[

        {"name": "Pays",
         "elements": [

             {"name": "France", "elements": []},
             {"name": "Emirats Arabes Unis", "elements": []},
             {"name": "Espagne", "elements": []},
             {"name": "Suisse", "elements": []},
             {"name": "Etats-Unis", "elements": []},
             {"name": "Arabie Saoudite", "elements": []},
             {"name": "Grande-Bretagne", "elements": []},
             {"name": "U.E.B.L", "elements": []},
             {"name": "Allemagne", "elements": []},
             {"name": "Irlande", "elements": []},
             {"name": "Pays-Bas", "elements": []},
             {"name": "Koweït", "elements": []},
             {"name": "Italie", "elements": []},
             {"name": "Singapour", "elements": []},
             {"name": "Danemark", "elements": []},
             {"name": "Inde", "elements": []},
             {"name": "Japon", "elements": []},
             {"name": "Lybie", "elements": []},
             {"name": "Suède", "elements": []},
             {"name": "Tunisie", "elements": []},
             {"name": "Corée du sud", "elements": []},
             {"name": "Portugal", "elements": []},
             {"name": "Pakistan", "elements": []},
             {"name": "Autres pays", "elements": []},

         ]},


    ]
    return IDE_Maroc_Stock_Par_Pays_hierarchy

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
#######################################################################################################################""
#######################################IDE_Maroc_Recettes_par_secteurs_NMA_hierarchy####################################
########################################################################################################################


@api.get("/IDE_Maroc_Recettes_par_secteurs_NMA/")
async def hierarchy():
    IDE_Maroc_Recettes_par_secteurs_NMA_hierarchy=[

        {"name": "Agriculture, sylviculture et pêche",
         "elements": [

             {"name": "Culture et production animale, chasse et services annexes", "elements": []},
             {"name": "Sylviculture et exploitation forestière", "elements": []},
             {"name": "Pêche et aquaculture", "elements": []}

         ]},
        {"name": "Industries extractives",
        "elements": [
            {"name": "Extraction de houille et de lignite", "elements": []},
            {"name": "Extraction d'hydrocarbures", "elements": []},
            {"name": "Extraction de minerais métalliques", "elements": []},
            {"name": "Autres industries extractives", "elements": []},
            {"name": "Services de soutien aux industries extractives", "elements": []}
        ]},
        {"name": "Industries manufacturières",
         "elements": [
             {"name": "Industries alimentaires", "elements": []},
             {"name": "Fabrication de boissons ", "elements": []},
             {"name": "Industrie du tabac", "elements": []},
             {"name": "Fabrication de textiles", "elements": []},
             {"name": "Industrie de l'habillement", "elements": []},
             {"name": "Industrie du cuir et de la chaussure", "elements": []},
             {"name": "Industrie du bois", "elements": []},
             {"name": "Industrie du papier et du carton", "elements": []},
             {"name": "Imprimerie et reproduction d'enregistrement", "elements": []},
             {"name": "Cokéfaction et raffinage", "elements": []},
             {"name": "Industrie chimique", "elements": []},
             {"name": "Industrie pharmaceutique", "elements": []},
             {"name": "Fabrication de produits en caoutchouc et en plastique", "elements": []},
             {"name": "Fabrication d'autres produits minéraux non métalliques", "elements": []},
             {"name": "Industrie métallurgique", "elements": []},
             {"name": "Fabrication de produits métalliques, à l'exception des machines et des équipements", "elements": []},
             {"name": "Fabrication de produits informatiques, électroniques et optiques", "elements": []},
             {"name": "Fabrication d'équipements électriques", "elements": []},
             {"name": "Industrie automobile", "elements": []},
             {"name": "Fabrication d'autres matériels de transport", "elements": []},
             {"name": "Fabrication de meubles", "elements": []},
             {"name": "Autres industries manufacturières", "elements": []},
             {"name": "Réparation et installation de machines et d'équipements", "elements": []}

         ]},
        {"name": "Electricité, gaz, vapeur et air conditionné", "elements": []},
        {"name": "Eau, assainissement, gestion des déchets et dépollution",
        "elements": [
            {"name": "Captage, traitement et distribution d'eau", "elements": []},
            {"name": "Collecte et traitement des eaux usées", "elements": []},
            {"name": "Collecte, traitement et élimination des déchets ; récupération", "elements": []},
            {"name": "Dépollution et autres services de gestion des déchets", "elements": []}

        ]},
        {"name": "Construction",
         "elements": [
             {"name": "Construction de bâtiments", "elements": []},
             {"name": "Génie civil", "elements": []},
             {"name": "Travaux de construction spécialisés", "elements": []}
         ]},
        {"name": "Commerce, réparation d'automobiles et de motocycles",
         "elements": [
             {"name": "Commerce et réparation d'automobiles et de motocycles", "elements": []},
             {"name": "Commerce de gros", "elements": []},
             {"name": "Commerce de détail", "elements": []}

         ]},
        {"name": "Transports et entreposage",
         "elements": [
             {"name": "Transports terrestres et transports par conduites", "elements": []},
             {"name": "Transports par eau", "elements": []},
             {"name": "Transports aériens ", "elements": []},
             {"name": "Entreposage et services auxiliaires des transports", "elements": []},
             {"name": "Activités de poste et de courrier", "elements": []}

         ]},
        {"name": "Hébergement et restauration",
         "elements": [
             {"name": "Hébergement", "elements": []},
             {"name": "Restauration", "elements": []}

         ]},
        {"name": "Information et communication",
         "elements": [
             {"name": "Édition", "elements": []},
             {"name": "Production de films cinématographiques, de vidéos et de programmes de télévision", "elements": []},
             {"name": "Programmation et diffusion", "elements": []},
             {"name": "Télécommunications", "elements": []},
             {"name": "Programmation, conseil et autres activités informatiques", "elements": []},
             {"name": "Services d'information", "elements": []}
         ]},
        {"name": "Activités financières et d'assurance",
         "elements": [
             {"name": "Activités des services financiers, hors assurance et caisses de retraite dont activités des sociétés holdings", "elements": []},
             {"name": "Assurance", "elements": []},
             {"name": "Activités auxiliaires de services financiers et d'assurance", "elements": []},

         ]},
        {"name": "Activités immobilières", "elements": []},
        {"name": "Activités spécialisées, scientifiques et techniques",
         "elements": [
             {"name": "Activités juridiques et comptables", "elements": []},
             {"name": "Activités des sièges sociaux et conseils de gestion", "elements": []},
             {"name": "Activités d'architecture, d'ingénierie, de contrôle et analyses tehniques", "elements": []},
             {"name": "Recherche-développement scientifique", "elements": []},
             {"name": "Publicité et études de marché", "elements": []},
             {"name": "Autres activités spécialisées, scientifiques et techniques", "elements": []}

         ]},
        {"name": "Autres services", "elements": []},
        {"name": "Divers secteurs", "elements": []}
    ]
    return IDE_Maroc_Recettes_par_secteurs_NMA_hierarchy



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
#######################################################################################################################""
#######################################IDE_Maroc_Recettes_par_secteurs_hierarchy####################################
########################################################################################################################

@api.get("/IDE_Maroc_Recettes_par_secteurs/")
async def hierarchy():
    IDE_Maroc_Recettes_par_secteurs_hierarchy=[

        {"name": "SECTEURS D'ACTIVITE",
         "elements": [

             {"name": "Industrie", "elements": []},
             {"name": "Immobilier", "elements": []},
             {"name": "Commerce", "elements": []},
             {"name": "Energie et mines", "elements": []},
             {"name": "Banque", "elements": []},
             {"name": "Tourisme", "elements": []},
             {"name": "Transports", "elements": []},
             {"name": "Holding", "elements": []},
             {"name": "Grands travaux", "elements": []},
             {"name": "Agriculture", "elements": []},
             {"name": "Assurances", "elements": []},
             {"name": "Etudes", "elements": []},
             {"name": "Télécommunications", "elements": []},
             {"name": "Pêche", "elements": []},
             {"name": "Autres services", "elements": []},
             {"name": "Divers secteurs", "elements": []}
         ]},

    ]
    return IDE_Maroc_Recettes_par_secteurs_hierarchy
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
#######################################################################################################################""
#######################################IDE_Maroc_Recettes_par_pays_hierarchy####################################
########################################################################################################################

@api.get("/IDE_Maroc_Recettes_par_pays/")
async def hierarchy():
    IDE_Maroc_Recettes_par_pays_hierarchy=[

        {"name": "PAYS/ORGANISMES FINANCIERS",
         "elements": [

             {"name": "France", "elements": []},

             {"name": "Emirats Arabes Unis", "elements": []},
             {"name": "Grande Bretagne", "elements": []},
             {"name": "Espagne", "elements": []},
             {"name": "Luxembourg", "elements": []},
             {"name": "Allemagne", "elements": []},
             {"name": "Pays Bas", "elements": []},
             {"name": "Qatar", "elements": []},
             {"name": "Maurice", "elements": []},
             {"name": "Afrique du Sud", "elements": []},
             {"name": "Italie", "elements": []},
             {"name": "Etats-Unis", "elements": []},
             {"name": "Suisse", "elements": []},
             {"name": "Irlande", "elements": []},
             {"name": "Bahreïn", "elements": []},

             {"name": "Malte", "elements": []},
             {"name": "Chine", "elements": []},
             {"name": "Belgique", "elements": []},
             {"name": "Arabie Saoudite", "elements": []},
             {"name": "Turquie", "elements": []},
             {"name": "Chypre", "elements": []},
             {"name": "République de Corée", "elements": []},

             {"name": "Fonds Arabe de Développement Economique et Social", "elements": []},
             {"name": "Singapour", "elements": []},
             {"name": "Canada", "elements": []},
             {"name": "Inde", "elements": []},

             {"name": "Suède", "elements": []},

             {"name": "Tunisie", "elements": []},
             {"name": "Oman", "elements": []},
             {"name": "Koweït", "elements": []},
             {"name": "Malaisie", "elements": []},
             {"name": "Portugal", "elements": []},

             {"name": "Monaco", "elements": []},
             {"name": "Roumanie", "elements": []},
             {"name": "Jersey", "elements": []},
             {"name": "Russie", "elements": []},
             {"name": "Grèce", "elements": []},
             {"name": "Danemark", "elements": []},


             {"name": "Hong-Kong", "elements": []},
             {"name": "Autriche", "elements": []},
             {"name": "Egypte", "elements": []},
             {"name": "Côte d'Ivoire", "elements": []},
             {"name": "Brésil", "elements": []},
             {"name": "Pologne", "elements": []},
             {"name": "Panama", "elements": []},
             {"name": "Japon", "elements": []},
             {"name": "Congo", "elements": []},
             {"name": "Islande", "elements": []},
             {"name": "Slovaquie", "elements": []},
             {"name": "Gabon", "elements": []},
             {"name": "Mauritanie", "elements": []},
             {"name": "Kenya", "elements": []},
             {"name": "Banque Islamique de Développement", "elements": []},


             {"name": "U.E.B.L", "elements": []},
             {"name": "Banque Africaine de Développement", "elements": []},
            
             {"name": "Autres pays", "elements": []}

         ]},

    ]
    return IDE_Maroc_Recettes_par_pays_hierarchy

###############################################################################################################
#################################IDE_Maroc_Recettes_par_pays_0################################################
@api.get('/IDE_Maroc_Recettes_par_pays_0/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IDE_Maroc_Recettes_par_pays_0.find({"Date": {"$gte": start, "$lte": end}},{"_id": 0, "Date": 1, "Pays ": 1, "Valeur": 1}));
    else:
        a = list(IDE_Maroc_Recettes_par_pays_0.find({}, {"_id": 0, "Date": 1, "Pays ": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

######################################################################################################################""
#######################################IDE_Maroc_Flux_Par_Nature_opération_hierarchy####################################
########################################################################################################################

@api.get("/IDE_Maroc_Flux_Par_Nature_opération/")
async def hierarchy():
    IDE_Maroc_Flux_Par_Nature_opération_hierarchy=[

        {"name": "Dépenses",
         "elements": [

             {"name": "Titres de participation", "elements": []},
             {"name": "Bénéfices réinvestis", "elements": []},
             {"name": "Instruments de dette", "elements": []},

         ]},
        {"name": "Recettes",
         "elements": [

             {"name": "Titres de participation", "elements": []},
             {"name": "Bénéfices réinvestis", "elements": []},
             {"name": "Instruments de dette", "elements": []},

         ]},
        {"name": "Flux net",
         "elements": [

             {"name": "Titres de participation", "elements": []},
             {"name": "Bénéfices réinvestis", "elements": []},
             {"name": "Instruments de dette", "elements": []},

         ]},

    ]
    return IDE_Maroc_Flux_Par_Nature_opération_hierarchy
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
 #######################################################################################################################""
#######################################IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_hierarchy####################################
########################################################################################################################

@api.get("/IDE_Maroc_Flux_flux_nets_par_secteurs_NMA/")
async def hierarchy():
    IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_hierarchy=[

        {"name": "Agriculture, sylviculture et pêche",
         "elements": [

             {"name": "Culture et production animale, chasse et services annexes", "elements": []},
             {"name": "Sylviculture et exploitation forestière", "elements": []},
             {"name": "Pêche et aquaculture", "elements": []}

         ]},
        {"name": "Industries extractives",
        "elements": [
            {"name": "Extraction d'hydrocarbures", "elements": []},
            {"name": "Extraction de minerais métalliques", "elements": []},
            {"name": "Autres industries extractives", "elements": []},
            {"name": "Services de soutien aux industries extractives", "elements": []}
        ]},
        {"name": "Industries manufacturières",
         "elements": [
             {"name": "Industries alimentaires", "elements": []},
             {"name": "Fabrication de boissons ", "elements": []},
             {"name": "Industrie du tabac", "elements": []},
             {"name": "Fabrication de textiles", "elements": []},
             {"name": "Industrie de l'habillement", "elements": []},
             {"name": "Industrie du cuir et de la chaussure", "elements": []},
             {"name": "Industrie du bois", "elements": []},
             {"name": "Industrie du papier et du carton", "elements": []},
             {"name": "Imprimerie et reproduction d'enregistrement", "elements": []},
             {"name": "Industrie chimique", "elements": []},
             {"name": "Industrie pharmaceutique", "elements": []},
             {"name": "Fabrication de produits en caoutchouc et en plastique", "elements": []},
             {"name": "Fabrication d'autres produits minéraux non métalliques", "elements": []},
             {"name": "Industrie métallurgique", "elements": []},
             {"name": "Fabrication de produits métalliques, à l'exception des machines et des équipements", "elements": []},
             {"name": "Fabrication de produits informatiques, électroniques et optiques", "elements": []},
             {"name": "Fabrication d'équipements électriques", "elements": []},
             {"name": "Industrie automobile", "elements": []},
             {"name": "Fabrication d'autres matériels de transport", "elements": []},
             {"name": "Fabrication de meubles", "elements": []},
             {"name": "Autres industries manufacturières", "elements": []},
             {"name": "Réparation et installation de machines et d'équipements", "elements": []}

         ]},
        {"name": "Electricité, gaz, vapeur et air conditionné",
        "elements": [
            {"name": "Captage, traitement et distribution d'eau", "elements": []},
            {"name": "Collecte et traitement des eaux usées", "elements": []},
            {"name": "Collecte, traitement et élimination des déchets ; récupération", "elements": []},
            {"name": "Dépollution et autres services de gestion des déchets", "elements": []}

        ]},
        {"name": "Construction",
         "elements": [
             {"name": "Construction de bâtiments", "elements": []},
             {"name": "Génie civil", "elements": []},
             {"name": "Travaux de construction spécialisés", "elements": []}
         ]},
        {"name": "Commerce, réparation d'automobiles et de motocycles",
         "elements": [
             {"name": "Commerce et réparation d'automobiles et de motocycles", "elements": []},
             {"name": "Commerce de gros", "elements": []},
             {"name": "Commerce de détail", "elements": []}

         ]},
        {"name": "Transports et entreposage",
         "elements": [
             {"name": "Transports terrestres et transports par conduites", "elements": []},
             {"name": "Transports par eau", "elements": []},
             {"name": "Transports aériens ", "elements": []},
             {"name": "Entreposage et services auxiliaires des transports", "elements": []},
             {"name": "Activités de poste et de courrier", "elements": []}

         ]},
        {"name": "Hébergement et restauration",
         "elements": [
             {"name": "Hébergement", "elements": []},
             {"name": "Restauration", "elements": []}

         ]},
        {"name": "Information et communication",
         "elements": [
             {"name": "Édition", "elements": []},
             {"name": "Production de films cinématographiques, de vidéos et de programmes de télévision", "elements": []},
             {"name": "Programmation et diffusion", "elements": []},
             {"name": "Télécommunications", "elements": []},
             {"name": "Programmation, conseil et autres activités informatiques", "elements": []},
             {"name": "Services d'information", "elements": []}
         ]},
        {"name": "Activités financières et d'assurance",
         "elements": [
             {"name": "Activités des services financiers, hors assurance et caisses de retraite dont activités des sociétés holdings", "elements": []},
             {"name": "Assurance", "elements": []},
             {"name": "Activités auxiliaires de services financiers et d'assurance", "elements": []},

         ]},
        {"name": "Activités immobilières", "elements": []},
        {"name": "Activités spécialisées, scientifiques et techniques",
         "elements": [
             {"name": "Activités juridiques et comptables", "elements": []},
             {"name": "Activités des sièges sociaux et conseils de gestion", "elements": []},
             {"name": "Activités d'architecture, d'ingénierie, de contrôle et analyses tehniques", "elements": []},
             {"name": "Recherche-développement scientifique", "elements": []},
             {"name": "Publicité et études de marché", "elements": []},
             {"name": "Autres activités spécialisées, scientifiques et techniques", "elements": []}

         ]},
        {"name": "Autres services", "elements": []},
        {"name": "Divers secteurs", "elements": []}
    ]
    return IDE_Maroc_Flux_flux_nets_par_secteurs_NMA_hierarchy


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
##########################################################################################################################################################""
############################################IDM_a_Etranger_Flux_Depenses_par_pays_hierarchy#################################################################
############################################################################################################################################################

@api.get("/IDM_a_Etranger_Flux_Depenses_par_pays/")
async def hierarchy():
    IDM_a_Etranger_Flux_Depenses_par_pays_hierarchy=[

        {"name": "PAYS DE DESTINATION",
         "elements": [

             {"name": "Côte d'Ivoire", "elements": []},
             {"name": "Emirats Arabes Unis", "elements": []},
             {"name": "Cameroun", "elements": []},
             {"name": "France", "elements": []},
             {"name": "Maurice", "elements": []},
             {"name": "Luxembourg", "elements": []},
             {"name": "Gabon", "elements": []},
             {"name": "Sénégal", "elements": []},
             {"name": "Burkina Faso", "elements": []},
             {"name": "Egypte", "elements": []},
             {"name": "Mali", "elements": []},
             {"name": "Suisse", "elements": []},
             {"name": "Guinée", "elements": []},
             {"name": "Congo", "elements": []},
             {"name": "Tunisie", "elements": []},
             {"name": "Madagascar", "elements": []},
             {"name": "Inde", "elements": []},
             {"name": "Ghana", "elements": []},
             {"name": "Nigéria", "elements": []},
             {"name": "Etats-Unis", "elements": []},
             {"name": "Bénin", "elements": []},
             {"name": "République Centrafricaine", "elements": []},
             {"name": "Portugal", "elements": []},
             {"name": "Uganda", "elements": []},
             {"name": "Togo", "elements": []},
             {"name": "Belgique", "elements": []},
             {"name": "Mauritanie", "elements": []},
             {"name": "Singapour", "elements": []},
             {"name": "Tchad", "elements": []},
             {"name": "Espagne", "elements": []},
             {"name": "Arabie Saoudite", "elements": []},
             {"name": "Pays-Bas", "elements": []},
             {"name": "Guinée-Bissau", "elements": []},
             {"name": "Kenya", "elements": []},
             {"name": "Algérie", "elements": []},
             {"name": "Allemagne", "elements": []},
             {"name": "Tanzanie", "elements": []},
             {"name": "Grande Bretagne", "elements": []},
             {"name": "Danemark", "elements": []},
             {"name": "Niger", "elements": []},
             {"name": "Liban", "elements": []},
             {"name": "Autriche", "elements": []},
             {"name": "Qatar", "elements": []},
             {"name": "Suède", "elements": []},
             {"name": "Bahrein", "elements": []},
             {"name": "Malte", "elements": []},
             {"name": "Monaco", "elements": []},
             {"name": "République Démocratique du Congo", "elements": []},
             {"name": "Jordanie", "elements": []},
             {"name": "Autres pays", "elements": []},
         ]},

    ]
    return IDM_a_Etranger_Flux_Depenses_par_pays_hierarchy

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

######################################################################################################################
#########################################IDM_a_etranger_Flux_Depenses_par_secteurs_hierarchy#########################
#####################################################################################################################
@api.get("/IDM_a_etranger_Flux_Depenses_par_secteurs/")
async def hierarchy():
    IDM_a_etranger_Flux_Depenses_par_secteurs_hierarchy=[

        {"name": "SECTEURS D'ACTIVITE",
         "elements": [
             {"name": "Banque", "elements": []},
             {"name": "Energie et mines", "elements": []},
             {"name": "Industrie", "elements": []},
             {"name": "Commerce", "elements": []},
             {"name": "Télécommunications", "elements": []},
             {"name": "Assurances", "elements": []},
             {"name": "Immobilier", "elements": []},
             {"name": "Grands travaux", "elements": []},
             {"name": "Holding", "elements": []},
             {"name": "Transport", "elements": []},
             {"name": "Etudes", "elements": []},
             {"name": "Tourisme", "elements": []},
             {"name": "Pêche", "elements": []},
             {"name": "Agriculture", "elements": []},
             {"name": "Autres services", "elements": []},
             {"name": "Divers secteurs", "elements": []},
         ]},

    ]
    return IDM_a_etranger_Flux_Depenses_par_secteurs_hierarchy


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
#######################################################################################################################""
#######################################IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_hierarchy####################################
########################################################################################################################

@api.get("/IDM_a_etranger_Flux_Depenses_par_secteurs_NMA/")
async def hierarchy():
    IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_hierarchy=[

        {"name": "Agriculture, sylviculture et pêche",
         "elements": [

             {"name": "Culture et production animale, chasse et services annexes", "elements": []},
             {"name": "Pêche et aquaculture", "elements": []}

         ]},
        {"name": "Industries extractives",
        "elements": [

            {"name": "Extraction d'hydrocarbures", "elements": []},
            {"name": "Extraction de minerais métalliques", "elements": []},
            {"name": "Autres industries extractives", "elements": []}

        ]},
        {"name": "Industries manufacturières",
         "elements": [
             {"name": "Industries alimentaires", "elements": []},
             {"name": "Fabrication de boissons ", "elements": []},
             {"name": "Industrie du tabac", "elements": []},
             {"name": "Fabrication de textiles", "elements": []},
             {"name": "Industrie de l'habillement", "elements": []},
             {"name": "Industrie du cuir et de la chaussure", "elements": []},
             {"name": "Industrie du bois", "elements": []},
             {"name": "Industrie du papier et du carton", "elements": []},

             {"name": "Industrie chimique", "elements": []},
             {"name": "Industrie pharmaceutique", "elements": []},
             {"name": "Fabrication de produits en caoutchouc et en plastique", "elements": []},
             {"name": "Fabrication d'autres produits minéraux non métalliques", "elements": []},
             {"name": "Industrie métallurgique", "elements": []},
             {"name": "Fabrication de produits métalliques, à l'exception des machines et des équipements", "elements": []},

             {"name": "Fabrication d'équipements électriques", "elements": []},

             {"name": "Fabrication de machines et équipements", "elements": []},
             {"name": "Fabrication automobile", "elements": []},

             {"name": "Fabrication d'autres matériels de transport", "elements": []},
             {"name": "Fabrication de meubles", "elements": []},
             {"name": "Autres industries manufacturières", "elements": []},
             {"name": "Réparation et installation de machines et d'équipements", "elements": []}

         ]},
        {"name": "Electricité, gaz, vapeur et air conditionné","elements": []},
        {"name": "Eau, assainissement, gestion des déchets et dépollution", 
        "elements": [
            {"name": "Captage, traitement et distribution d'eau", "elements": []},
           
            {"name": "Collecte, traitement et élimination des déchets ; récupération", "elements": []},
            {"name": "Dépollution et autres services de gestion des déchets", "elements": []}

        ]},
        {"name": "Construction",
         "elements": [
             {"name": "Construction de bâtiments", "elements": []},
             {"name": "Génie civil", "elements": []},
             {"name": "Travaux de construction spécialisés", "elements": []}
         ]},
        {"name": "Commerce, réparation d'automobiles et de motocycles",
         "elements": [
             {"name": "Commerce et réparation d'automobiles et de motocycles", "elements": []},
             {"name": "Commerce de gros", "elements": []},
             {"name": "Commerce de détails", "elements": []}

         ]},
        {"name": "Transports et entreposage",
         "elements": [
             {"name": "Transports terrestres et transports par conduites", "elements": []},
             {"name": "Transports par eau", "elements": []},
             {"name": "Transports aériens ", "elements": []},
             {"name": "Entreposage et services auxiliaires des transports", "elements": []}
            

         ]},
        {"name": "Hébergement et restauration",
         "elements": [
             {"name": "Hébergement", "elements": []},
             {"name": "Restauration", "elements": []}

         ]},
        {"name": "Information et communication",
         "elements": [
             {"name": "Édition", "elements": []},
             {"name": "Production de films cinématographiques, de vidéos et de programmes de télévision", "elements": []},
             {"name": "Programmation et diffusion", "elements": []},
             {"name": "Télécommunications", "elements": []},
             {"name": "Programmation, conseil et autres activités informatiques", "elements": []},
             {"name": "Services d'information", "elements": []}
         ]},
        {"name": "Activités financières et d'assurance",
         "elements": [
             {"name": "Activités des services financiers, hors assurance et caisses de retraite dont activités des sociétés holdings", "elements": []},
             {"name": "Assurance", "elements": []},
             {"name": "Activités auxiliaires de services financiers et d'assurance", "elements": []},

         ]},
        {"name": "Activités immobilières", "elements": []},
        {"name": "Activités spécialisées, scientifiques et techniques",
         "elements": [
             {"name": "Activités juridiques et comptables", "elements": []},
             {"name": "Activités des sièges sociaux et conseils de gestion", "elements": []},
             {"name": "Activités d'architecture, d'ingénierie, de contrôle et analyses tehniques", "elements": []},
       
             {"name": "Publicité et études de marché", "elements": []},
             {"name": "Autres activités spécialisées, scientifiques et techniques", "elements": []}

         ]},
        {"name": "Autres services", "elements": []},
        {"name": "Divers secteurs", "elements": []}
    ]
    return IDM_a_etranger_Flux_Depenses_par_secteurs_NMA_hierarchy


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
##################################""IDM_a_Etranger_Flux_Flux_nets_par_pays_hierarchy#############################
#################################################################################################################
@api.get("/IDM_a_Etranger_Flux_Flux_nets_par_pays/")
async def hierarchy():
    IDM_a_Etranger_Flux_Flux_nets_par_pays_hierarchy=[

        {"name": "PAYS DE DESTINATION",
         "elements": [
             {"name": "Emirats Arabes Unis", "elements": []},
             {"name": "Côte d'Ivoire", "elements": []},
             {"name": "Cameroun", "elements": []},
             {"name": "Luxembourg", "elements": []},
             {"name": "Gabon", "elements": []},
             {"name": "Burkina Faso", "elements": []},
             {"name": "Sénégal", "elements": []},
             {"name": "France", "elements": []},
             {"name": "Egypte", "elements": []},
             {"name": "Mali", "elements": []},
             {"name": "Suisse", "elements": []},
             {"name": "Guinée", "elements": []},
             {"name": "Madagascar", "elements": []},
             {"name": "Inde", "elements": []},
             {"name": "Tunisie", "elements": []},
             {"name": "Ghana", "elements": []},
             {"name": "Congo", "elements": []},
             {"name": "Nigéria", "elements": []},
             {"name": "Etats-Unis", "elements": []},
             {"name": "Portugal", "elements": []},
             {"name": "Uganda", "elements": []},
             {"name": "Mauritanie", "elements": []},
             {"name": "Singapour", "elements": []},
             {"name": "Togo", "elements": []},
             {"name": "Belgique", "elements": []},
             {"name": "Arabie Saoudite", "elements": []},
             {"name": "Pays-Bas", "elements": []},
             {"name": "Grande Bretagne", "elements": []},
             {"name": "Autriche", "elements": []},
             {"name": "Suède", "elements": []},
             {"name": "Iles Vierges Britaniques", "elements": []},
             {"name": "Norvège", "elements": []},
             {"name": "Australie", "elements": []},
             {"name": "Monaco", "elements": []},
             {"name": "Soudan", "elements": []},
             {"name": "République Démocratique du Congo", "elements": []},
             {"name": "Malte", "elements": []},
             {"name": "Allemagne", "elements": []},
             {"name": "Guinée-Bissau", "elements": []},
             {"name": "Maurice", "elements": []},
             {"name": "Tanzanie", "elements": []},
             {"name": "Espagne", "elements": []},
             {"name": "République Centrafricaine", "elements": []},
             {"name": "Liban", "elements": []},
             {"name": "Tchad", "elements": []},
             {"name": "Niger", "elements": []},
             {"name": "Bénin", "elements": []},
             {"name": "Autres pays", "elements": []},
         ]},

    ]
    return IDM_a_Etranger_Flux_Flux_nets_par_pays_hierarchy


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
#####################################################################################################################"
######################################IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_hierarchy########################
#######################################################################################################################
@api.get("/IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA/")
async def hierarchy():
    IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_hierarchy=[

        {"name": "Agriculture sylviculture et pêche",
         "elements": [
             {"name": "Culture et production animale, chasse et services annexes", "elements": []},
             {"name": "Pêche et aquaculture", "elements": []}
         ]},
        {"name": "Industries extractives",
         "elements": [
             {"name": "Extraction d'hydrocarbures", "elements": []},
             {"name": "Extraction de minerais métalliques", "elements": []},
             {"name": "Autres industries extractives", "elements": []}
         ]},
        {"name": "Industries manufacturières",
         "elements": [
             {"name": "Industries alimentaires", "elements": []},
             {"name": "Fabrication de boissons", "elements": []},
             {"name": "Industrie du tabac", "elements": []},
             {"name": "Fabrication de textiles", "elements": []},
             {"name": "Industrie de l'habillement", "elements": []},
             {"name": "Industrie du cuir et de la chaussure", "elements": []},
             {"name": "Industrie du bois", "elements": []},
             {"name": "Industrie du papier et du carton", "elements": []},
             {"name": "Industrie chimique", "elements": []},
             {"name": "Industrie pharmaceutique", "elements": []},
             {"name": "Fabrication de produits en caoutchouc et en plastique", "elements": []},
             {"name": "Fabrication d'autres produits minéraux non métalliques", "elements": []},
             {"name": "Industrie métallurgique", "elements": []},
             {"name": "Fabrication de produits métalliques, à l'exception des machines et des équipements", "elements": []},
             {"name": "Fabrication d'équipements électriques", "elements": []},
             {"name": "Fabrication de machines et équipements", "elements": []},
             {"name": "Fabrication automobile", "elements": []},
             {"name": "Fabrication d'autres matériels de transport", "elements": []},
             {"name": "Fabrication de meubles ", "elements": []},
             {"name": "Autres industries manufacturières", "elements": []},
             {"name": "Réparation et installation de machines et d'équipements", "elements": []}
         ]},

        {"name": "Electricité, gaz, vapeur et air conditionné","elements": []},
        {"name": "Eau, assainissement, gestion des déchets et dépollution",
         "elements": [
             {"name": "Captage, traitement et distribution d'eau", "elements": []},
             {"name": "Collecte, traitement et élimination des déchets; récupération", "elements": []},
             {"name": "Dépollution et autres services de gestion des déchets", "elements": []}
         ]},
        {"name": "Construction",
         "elements": [
             {"name": "Construction de bâtiments", "elements": []},
             {"name": "Génie civil", "elements": []},
             {"name": "Travaux de construction spécialisés", "elements": []}
         ]},
        {"name": "Commerce, réparation d'automobiles et de motocycles",
         "elements": [
             {"name": "Commerce et réparation d'automobiles et de motocycles", "elements": []},
             {"name": "Commerce de gros", "elements": []},
             {"name": "Commerce de détails", "elements": []}
         ]},
        {"name": "Transports et entreposage",
         "elements": [
             {"name": "Transports terrestres et transports par conduites", "elements": []},
             {"name": "CTransport par eau", "elements": []},
             {"name": "Transports aériens", "elements": []},
             {"name": "TEntreposage et services auxiliaires des transports", "elements": []}
         ]},
        {"name": "Hébergement et restauration",
         "elements": [
             {"name": "Hébergement", "elements": []},
             {"name": "Restauration", "elements": []}
         ]},
        {"name": "Information et communication",
         "elements": [
             {"name": "Édition", "elements": []},
             {"name": "Production de films cinématographiques, de vidéo et de programme de télévision", "elements": []},
             {"name": "Programme et diffusion", "elements": []},
             {"name": "Télécommunication", "elements": []},
             {"name": "Programmation, conseil et autres activités informatiques", "elements": []},
             {"name": "Service d'information", "elements": []}
         ]},
        {"name": "Activités financières et d'assurance",
         "elements": [
             {"name": "Activités des services financiers, hors assurance et caisses de retraite dont activités des sociétés holdings", "elements": []},
             {"name": "Assurance", "elements": []},
             {"name": "Activités auxiliaires de services financiers et d'assurance", "elements": []},

         ]},
        {"name": "Activités immobilières", "elements": []},
        {"name": "Activités spécialisées, scientifiques et techniques",
        "elements": [
            {"name": "Activités juridiques et comptables", "elements": []},
            {"name": "Activités des sièges sociaux et conseils de gestion", "elements": []},
            {"name": "Activités d'architecture, d'ingénierie, de contrôle et analyses techniques", "elements": []},
            {"name": "Publicité et études de marché", "elements": []},
            {"name": "Autres activités spécialisées, scientifiques et techniques", "elements": []},
        ]},
        {"name": "Autres services", "elements": []},
        {"name": "Divers secteurs", "elements": []},

    ]
    return IDM_a_Etranger_Flux_Flux_nets_par_secteurs_NMA_hierarchy


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
#######################################################################################################################""
#######################################IDM_etranger_flux_par_nat_operation_hierarchy####################################
########################################################################################################################

@api.get("/IDM_etranger_flux_par_nat_operation/")
async def hierarchy():
    IDM_etranger_flux_par_nat_operation_hierarchy=[

        {"name": "Dépenses",
         "elements": [

             {"name": "Titres de participation", "elements": []},
             {"name": "Bénéfices réinvestis", "elements": []},
             {"name": "Instruments de dette", "elements": []},

         ]},
        {"name": "Recettes",
         "elements": [

             {"name": "Titres de participation", "elements": []},
             {"name": "Bénéfices réinvestis", "elements": []},
             {"name": "Instruments de dette", "elements": []},

         ]},
        {"name": "Flux net",
         "elements": [

             {"name": "Titres de participation", "elements": []},
             {"name": "Bénéfices réinvestis", "elements": []},
             {"name": "Instruments de dette", "elements": []},

         ]},

    ]
    return IDM_etranger_flux_par_nat_operation_hierarchy


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
#######################################################################################################################
####################################IDM_a_etranger_Stock_Par_pays_hierarchy#############################################
#######################################################################################################################
@api.get("/IDM_a_etranger_Stock_Par_pays/")
async def hierarchy():
    IDM_a_etranger_Stock_Par_pays_hierarchy=[

        {"name": "PAYS",
         "elements": [
             {"name": "Côte d'Ivoire", "elements": []},
             {"name": "Luxembourg", "elements": []},
             {"name": "France", "elements": []},
             {"name": "Maurice", "elements": []},
             {"name": "Egypte", "elements": []},
             {"name": "Grande Bretagne", "elements": []},
             {"name": "Gabon", "elements": []},
             {"name": "Suisse", "elements": []},
             {"name": "Cameroun", "elements": []},
             {"name": "Mali", "elements": []},
             {"name": "Bénin", "elements": []},
             {"name": "Sénégal", "elements": []},
             {"name": "Burkina Faso", "elements": []},
             {"name": "Pays Bas", "elements": []},
             {"name": "Liban", "elements": []},
             {"name": "Congo", "elements": []},
             {"name": "Arabie saoudite", "elements": []},
             {"name": "Emirats Arabes Unis", "elements": []},
             {"name": "Belgique", "elements": []},
             {"name": "Mauritanie ", "elements": []},
             {"name": "Togo", "elements": []},
             {"name": "République Centrafricaine", "elements": []},
             {"name": "Niger", "elements": []},
             {"name": "Ghana", "elements": []},
             {"name": "Inde", "elements": []},
             {"name": "Tchad", "elements": []},
             {"name": "Espagne", "elements": []},
             {"name": "Guinée", "elements": []},
             {"name": "Tunisie", "elements": []},
             {"name": "Guinée-Bissau", "elements": []},
             {"name": "Nigeria", "elements": []},
             {"name": "Etats-Unis", "elements": []},
             {"name": "Malte", "elements": []},
             {"name": "Algérie", "elements": []},
             {"name": "Soudan", "elements": []},
             {"name": "Iles Vierges Britanniques", "elements": []},
             {"name": "Irlande", "elements": []},
             {"name": "République Démocratique du Congo", "elements": []},
             {"name": "Afrique du sud", "elements": []},
             {"name": "Guinée Equatoriale", "elements": []},
             {"name": "Guyana", "elements": []},
             {"name": "Autres pays", "elements": []},


         ]},
    ]
    return IDM_a_etranger_Stock_Par_pays_hierarchy


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
#######################################################################################################################
#######################################"IDM_à_etranger_Stock_Par_secteurs_hierarchy####################################
#######################################################################################################################
@api.get("/IDM_à_etranger_Stock_Par_secteurs/")
async def hierarchy():
    IDM_à_etranger_Stock_Par_secteurs_hierarchy = [

        {"name": "Secteurs",
         "elements": [
             {"name": "Banques et activités financières", "elements": []},
             {"name": "Immobilier", "elements": []},
             {"name": "Télécommunications", "elements": []},
             {"name": "Cimenteries", "elements": []},
             {"name": "Industrie", "elements": []},
             {"name": "Assurances", "elements": []},
             {"name": "Holding", "elements": []},
             {"name": "Energie et mines", "elements": []},
             {"name": "Commerce", "elements": []},
             {"name": "Transport", "elements": []},
             {"name": "Services informatiques", "elements": []},
             {"name": "Construction et génie civil", "elements": []},
             {"name": "Autres services ", "elements": []},
             {"name": "Divers secteurs", "elements": []},

         ]},
    ]
    return IDM_à_etranger_Stock_Par_secteurs_hierarchy

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
####################################################################################################################
######################################imp_services_nature_avant2014_hierarchy#######################################
######################################################################################################################
@api.get("/imp_services_nature_avant2014/")
async def hierarchy():
    imp_services_nature_avant2014_hierarchy=[

        {"name": "Importations:",
         "elements": [
             {"name": "Transports", "elements": []},
             {"name": "Voyages", "elements": []},
             {"name": "Services de communication", "elements": []},
             {"name": "Services d'assurance", "elements": []},
             {"name": "Redevances et droits de licence", "elements": []},
             {"name": "Autres services aux entreprises", "elements": []},
             {"name": "Services fournis ou reçus par les administrations publiques N.C.A", "elements": []}

         ]},
    ]
    return imp_services_nature_avant2014_hierarchy



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
####################################################################################################################
####################################"Imp_Services_Nature_depuis2014_hierarchy########################################
######################################################################################################################
@api.get("/Imp_Services_Nature_depuis2014/")
async def hierarchy():
    Imp_Services_Nature_depuis2014_hierarchy = [

        {"name": "Importations:",
         "elements": [
             {"name": "Services de fabrication fournis sur des intrants physiques  détenus par des tiers",
              "elements": []},
             {"name": "Services d’entretien et de réparation n.i.a.", "elements": []},
             {"name": "Transports", "elements": []},
             {"name": "Voyages", "elements": []},
             {"name": "Constructions", "elements": []},
             {"name": "Services d’assurance et de pension", "elements": []},
             {"name": "Services financiers", "elements": []},
             {"name": "Frais pour usage de la propriété intellectuelle n.i.a.", "elements": []},
             {"name": "Services de télécommunications, d’informatique et d’information", "elements": []},
             {"name": "Autres services aux entreprises", "elements": []},
             {"name": "Services personnels, culturels et relatifs aux loisirs", "elements": []},
             {"name": "Biens et services des administrations publiques n.i.a.", "elements": []},

         ]},
    ]
    return Imp_Services_Nature_depuis2014_hierarchy

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
######################################################################################################################
###########################################Exp_services_nature_4_avant2014###########################################
######################################################################################################################
@api.get("/Exp_services_nature_avant2014/")
async def hierarchy():
    Exp_services_nature_avant2014_hierarchy=[

        {"name": "Exportations:",
         "elements": [
             {"name": "Transports", "elements": []},
             {"name": "Voyages", "elements": []},
             {"name": "Services de communication", "elements": []},
             {"name": "Services d'assurance", "elements": []},
             {"name": "Redevances et droits de licence", "elements": []},
             {"name": "Autres services aux entreprises", "elements": []},
             {"name": "Services fournis ou reçus par les administrations publiques N.C.A", "elements": []}

         ]},
    ]
    return Exp_services_nature_avant2014_hierarchy


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
########################################Exp_Services_Nature_depuis2014_hierarchy#######################################
#######################################################################################################################
@api.get("/Exp_Services_Nature_depuis2014/")
async def hierarchy():
    Exp_Services_Nature_depuis2014_hierarchy=[

        {"name": "Exportations",
         "elements": [
             {"name": "Services de fabrication fournis sur des intrants physiques  détenus par des tiers", "elements": []},
             {"name": "Services d’entretien et de réparation n.i.a.", "elements": []},
             {"name": "Transports", "elements": []},
             {"name": "Voyages", "elements": []},
             {"name": "Constructions", "elements": []},
             {"name": "Services d’assurance et de pension", "elements": []},
             {"name": "Services financiers", "elements": []},
             {"name": "Frais pour usage de la propriété intellectuelle n.i.a.", "elements": []},
             {"name": "Services de télécommunications, d’informatique et d’information", "elements": []},
             {"name": "Autres services aux entreprises", "elements": []},
             {"name": "Services personnels, culturels et relatifs aux loisirs", "elements": []},
             {"name": "Biens et services des administrations publiques n.i.a.", "elements": []},


         ]},
    ]
    return Exp_Services_Nature_depuis2014_hierarchy

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
######################################################################################################################
#########################################Offshoring__hierarchy#################################################################
###############################################################################################################################
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

#######################################################################################
########################################################################################################################
#############################################BP_A_MBP5_divisé par 5################################################################################
########################################################################################################################


################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_solde_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_A_MBP5_CTC_solde/")
async def hierarchy():
    BP_A_MBP5_CTC_solde_hierarchy=[


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
            },


     ]
    return BP_A_MBP5_CTC_solde_hierarchy
################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_solde_historique######################################################################
###############################################################################################################################################################
@api.get('/BP_A_MBP5_CTC_solde_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5_CTC_solde.find({"Date": {"$gte": start, "$lte": end}},{"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,"Valeur": 1}));
    else:
        a = list(BP_A_MBP5_CTC_solde.find({}, {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,"Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

##################################################################################################################################################################
################################################################################################################################################################
##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_credit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_A_MBP5_CTC_credit/")
async def hierarchy():
    BP_A_MBP5_CTC_credit_hierarchy = [

        {"name": "COMPTE DES TRANSACTIONS COURANTES",
         "elements": [
             {"name": "BIENS",
              "elements": [
                  {"name": "Marchandises générales", "elements": []},
                  {"name": "Biens importés sans paiement et réexportés après transformation", "elements": []},
                  {"name": "Achats de biens dans les ports", "elements": []},
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
         ]},

    ]
    return BP_A_MBP5_CTC_credit_hierarchy

################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_credit_Historique######################################################################
###############################################################################################################################################################

@api.get('/BP_A_MBP5_CTC_credit/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5_CTC_credit.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_A_MBP5_CTC_credit.find({}, {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_debit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_A_MBP5_CTC_debit/")
async def hierarchy():
    BP_A_MBP5_CTC_debit_hierarchy=[

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
                       {"name": "Transports maritimes", "elements": []},
                       {"name": "Transports aériens", "elements": []},
                       {"name": "Autres transports", "elements": []},
                   ]
                   },
                  {"name": "Voyages",
                   "elements": [
                       {"name": "Voyages à titre professionnel", "elements": []},
                       {"name": "Voyages à titre personnel", "elements": []},
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
]
    return BP_A_MBP5_CTC_debit_hierarchy


################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_debit_Historique######################################################################
###############################################################################################################################################################
@api.get('/BP_A_MBP5_CTC_debit/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5_CTC_debit.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_A_MBP5_CTC_debit.find({}, {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_COF_credit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_A_MBP5_COF_credit/")
async def hierarchy():
    BP_A_MBP5_COF_credit_hierarchy=[


             {"name": "COMPTE DES OPERATIONS FINANCIERES",
              "elements": [
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
                            {"name": "Administrations", "elements": []},
                            {"name": "Banques", "elements": []},
                            {"name": "Autres secteurs", "elements": []},
                        ]},
                       {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                       {"name": "Autres OF", "elements": []},
                   ]},
                  {"name": "Avoirs de réserve ", "elements": []}
              ]},

    ]


    return BP_A_MBP5_COF_credit_hierarchy
##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_COF_credit_historique######################################################################
###############################################################################################################################################################

@api.get('/BP_A_MBP5_COF_credit/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5_COF_credit.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_A_MBP5_COF_credit.find({}, {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))




##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_COF_debit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_A_MBP5_COF_debit/")
async def hierarchy():
    BP_A_MBP5_COF_debit_hierarchy=[
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
                   "elements": [
                       {"name": "Administrations", "elements": []},
                       {"name": "Banques", "elements": []},
                       {"name": "Autres secteurs", "elements": []}
                   ]},
                  {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                  {"name": "Autres", "elements": []}
              ]},
             {"name": "Avoirs de réserve ", "elements": []}
         ]},

    ]
    return BP_A_MBP5_COF_debit_hierarchy

##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_COF_debit_historique######################################################################
###############################################################################################################################################################
@api.get('/BP_A_MBP5_COF_debit/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5_COF_debit.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_A_MBP5_COF_debit.find({}, {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

#######################################################################################
########################################################################################################################
#############################################BP_A_MBP5_divisé par 5################################################################################
########################################################################################################################


################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_solde_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_A_MBP5_CTC_solde/")
async def hierarchy():
    BP_A_MBP5_CTC_solde_hierarchy=[


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
            },


     ]
    return BP_A_MBP5_CTC_solde_hierarchy
################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_solde_historique######################################################################
###############################################################################################################################################################
@api.get('/BP_A_MBP5_CTC_solde_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5_CTC_solde.find({"Date": {"$gte": start, "$lte": end}},{"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,"Valeur": 1}));
    else:
        a = list(BP_A_MBP5_CTC_solde.find({}, {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,"Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

##################################################################################################################################################################
################################################################################################################################################################
##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_credit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_A_MBP5_CTC_credit/")
async def hierarchy():
    BP_A_MBP5_CTC_credit_hierarchy = [

        {"name": "COMPTE DES TRANSACTIONS COURANTES",
         "elements": [
             {"name": "BIENS",
              "elements": [
                  {"name": "Marchandises générales", "elements": []},
                  {"name": "Biens importés sans paiement et réexportés après transformation", "elements": []},
                  {"name": "Achats de biens dans les ports", "elements": []},
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
         ]},

    ]
    return BP_A_MBP5_CTC_credit_hierarchy

################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_credit_Historique######################################################################
###############################################################################################################################################################

@api.get('/BP_A_MBP5_CTC_credit/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5_CTC_credit.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_A_MBP5_CTC_credit.find({}, {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_debit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_A_MBP5_CTC_debit/")
async def hierarchy():
    BP_A_MBP5_CTC_debit_hierarchy=[

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
                       {"name": "Transports maritimes", "elements": []},
                       {"name": "Transports aériens", "elements": []},
                       {"name": "Autres transports", "elements": []},
                   ]
                   },
                  {"name": "Voyages",
                   "elements": [
                       {"name": "Voyages à titre professionnel", "elements": []},
                       {"name": "Voyages à titre personnel", "elements": []},
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
]
    return BP_A_MBP5_CTC_debit_hierarchy


################################################################################################################################################################
#############################################################BP_A_MBP5_CTC_debit_Historique######################################################################
###############################################################################################################################################################
@api.get('/BP_A_MBP5_CTC_debit/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5_CTC_debit.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_A_MBP5_CTC_debit.find({}, {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_COF_credit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_A_MBP5_COF_credit/")
async def hierarchy():
    BP_A_MBP5_COF_credit_hierarchy=[


             {"name": "COMPTE DES OPERATIONS FINANCIERES",
              "elements": [
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
                            {"name": "Administrations", "elements": []},
                            {"name": "Banques", "elements": []},
                            {"name": "Autres secteurs", "elements": []},
                        ]},
                       {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                       {"name": "Autres OF", "elements": []},
                   ]},
                  {"name": "Avoirs de réserve ", "elements": []}
              ]},

    ]


    return BP_A_MBP5_COF_credit_hierarchy
##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_COF_credit_historique######################################################################
###############################################################################################################################################################

@api.get('/BP_A_MBP5_COF_credit/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5_COF_credit.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_A_MBP5_COF_credit.find({}, {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))




##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_COF_debit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_A_MBP5_COF_debit/")
async def hierarchy():
    BP_A_MBP5_COF_debit_hierarchy=[
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
                   "elements": [
                       {"name": "Administrations", "elements": []},
                       {"name": "Banques", "elements": []},
                       {"name": "Autres secteurs", "elements": []}
                   ]},
                  {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                  {"name": "Autres", "elements": []}
              ]},
             {"name": "Avoirs de réserve ", "elements": []}
         ]},

    ]
    return BP_A_MBP5_COF_debit_hierarchy

##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_A_MBP5_COF_debit_historique######################################################################
###############################################################################################################################################################
@api.get('/BP_A_MBP5_COF_debit/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP5_COF_debit.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_A_MBP5_COF_debit.find({}, {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

#######################################################################################
########################################################################################################################
#############################################BP_T_MBP5_divisé par 5################################################################################
########################################################################################################################

################################################################################################################################################################
#############################################################BP_T_MBP5_CTC_solde_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_T_MBP5_CTC_SOLDE/")
async def hierarchy():
    BP_T_MBP5_CTC_SOLDE_hierarchy=[


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
            },


     ]
    return BP_T_MBP5_CTC_SOLDE_hierarchy
################################################################################################################################################################
#############################################################BP_T_MBP5_CTC_solde_historique######################################################################
###############################################################################################################################################################
@api.get('/BP_T_MBP5_CTC_SOLDE_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_T_MBP5_CTC_SOLDE.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                  "Valeur": 1}));
    else:
        a = list(BP_T_MBP5_CTC_SOLDE.find({}, {"_id": 0, "Date": 1,"P�riode":1,"Balance des paiements ": 1, "Cat�gorie": 1,
                                      "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

##################################################################################################################################################################
################################################################################################################################################################
##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_T_MBP5_CTC_credit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_T_MBP5_CTC_CREDIT/")
async def hierarchy():
    BP_T_MBP5_CTC_CREDIT_hierarchy = [

        {"name": "COMPTE DES TRANSACTIONS COURANTES",
         "elements": [
             {"name": "BIENS",
              "elements": [
                  {"name": "Marchandises générales", "elements": []},
                  {"name": "Biens importés sans paiement et réexportés après transformation", "elements": []},
                  {"name": "Achats de biens dans les ports", "elements": []},
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
         ]},

    ]
    return BP_T_MBP5_CTC_CREDIT_hierarchy

################################################################################################################################################################
#############################################################BP_T_MBP5_CTC_credit_Historique######################################################################
###############################################################################################################################################################

@api.get('/BP_T_MBP5_CTC_CREDIT/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_T_MBP5_CTC_CREDIT.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_T_MBP5_CTC_CREDIT.find({}, {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_T_MBP5_CTC_debit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_T_MBP5_CTC_DEBIT/")
async def hierarchy():
    BP_T_MBP5_CTC_DEBIT_hierarchy=[

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
                       {"name": "Transports maritimes", "elements": []},
                       {"name": "Transports aériens", "elements": []},
                       {"name": "Autres transports", "elements": []},
                   ]
                   },
                  {"name": "Voyages",
                   "elements": [
                       {"name": "Voyages à titre professionnel", "elements": []},
                       {"name": "Voyages à titre personnel", "elements": []},
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
]
    return BP_T_MBP5_CTC_DEBIT_hierarchy


################################################################################################################################################################
#############################################################BP_T_MBP5_CTC_debit_Historique######################################################################
###############################################################################################################################################################
@api.get('/BP_T_MBP5_CTC_DEBIT/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_T_MBP5_CTC_DEBIT.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_T_MBP5_CTC_DEBIT.find({}, {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_T_MBP5_COF_credit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_T_MBP5_COF_CREDIT/")
async def hierarchy():
    BP_T_MBP5_COF_CREDIT_hierarchy=[


             {"name": "COMPTE DES OPERATIONS FINANCIERES",
              "elements": [
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
                            {"name": "Administrations", "elements": []},
                            {"name": "Banques", "elements": []},
                            {"name": "Autres secteurs", "elements": []},
                        ]},
                       {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                       {"name": "Autres OF", "elements": []},
                   ]},
                  {"name": "Avoirs de réserve ", "elements": []}
              ]},

    ]


    return BP_T_MBP5_COF_CREDIT_hierarchy
##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_T_MBP5_COF_credit_historique######################################################################
###############################################################################################################################################################

@api.get('/BP_T_MBP5_COF_CREDIT/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_T_MBP5_COF_CREDIT.find({"Date": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Date": 1, "P�riode":1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                 "Nature de l'op�ration": 1, "Valeur": 1}));
    else:
        a = list(BP_T_MBP5_COF_CREDIT.find({}, {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,
                                     "Type": 1,"Segment": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))




##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_T_MBP5_COF_debit_hierarchy######################################################################
###############################################################################################################################################################
@api.get("/BP_T_MBP5_COF_DEBIT/")
async def hierarchy():
    BP_T_MBP5_COF_DEBIT_hierarchy=[
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
                   "elements": [
                       {"name": "Administrations", "elements": []},
                       {"name": "Banques", "elements": []},
                       {"name": "Autres secteurs", "elements": []}
                   ]},
                  {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                  {"name": "Autres", "elements": []}
              ]},
             {"name": "Avoirs de réserve ", "elements": []}
         ]},

    ]
    return BP_T_MBP5_COF_DEBIT_hierarchy

##################################################################################################################################################################
################################################################################################################################################################
#############################################################BP_T_MBP5_COF_debit_historique######################################################################
###############################################################################################################################################################
@api.get('/BP_T_MBP5_COF_DEBIT/Historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_T_MBP5_COF_DEBIT.find({"Date": {"$gte": start, "$lte": end}}, {"_id": 0, "Date": 1, "P�riode":1, "Balance des paiements ": 1, "Cat�gorie": 1,"Type": 1, "Segment": 1, "Valeur": 1}));
    else:
        a = list(BP_T_MBP5_COF_DEBIT.find({}, {"_id": 0, "Date": 1,"P�riode":1,  "Balance des paiements ": 1, "Cat�gorie": 1,"Type": 1,"Segment": 1, "Valeur": 1}));

    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#####################################################################################################################
############################################################################################################################
########################################################################################################################
#############################################BP_A_MBP6_divisé par 5################################################################################
########################################################################################################################



###############################################################################################################################################################
##############################################BP_A_MBP6_CTC_SOLDE_hierrarchy#######################################"4
############################################################################################################################
@api.get("/BP_A_MBP6_CTC_SOLDE/")
async def hierarchy():
    BP_A_MBP6_CTC_SOLDE_hierarchy = [


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
            },

    ]
    return BP_A_MBP6_CTC_SOLDE_hierarchy

##############################################################################################################################
#####################################BP_A_MBP6_CTC_SOLDE_HISTORIQUE#####################################################################
#############################################################################################################################
@api.get('/BP_A_MBP6_CTC_SOLDE_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_A_MBP6_CTC_SOLDE.find({"date": {"$gte": start, "$lte": end}},
                                  {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,"Valeur": 1}));
    else:
        a = list(BP_A_MBP6_CTC_SOLDE.find({},
                                  {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
####################################################################################################################################################
################################################################BP_A_MBP6_CTC_CREDIT_hierarchy###############################################################################################################################################################################################


@api.get("/BP_A_MBP6_CTC_CREDIT/")
async def hierarchy():
    BP_A_MBP6_CTC_CREDIT_hierarchy = [

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
            ]},
    ]
    return BP_A_MBP6_CTC_CREDIT_hierarchy

    ############################################################################################################################
    ########################################BP_A_MBP6_CTC_CREDIT_HISTORIQUE#####################################################
    ##########################################################################################################################"
@api.get('/BP_A_MBP6_CTC_CREDIT_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
        if (start and end):
            a = list(BP_A_MBP6_CTC_CREDIT.find({"date": {"$gte": start, "$lte": end}},
                                               {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                                "Type de compte": 1,
                                                "Type": 1, "Segment": 1, "Valeur": 1}));
        else:
            a = list(BP_A_MBP6_CTC_CREDIT.find({},
                                               {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                                "Type de compte": 1,
                                                "Type": 1, "Segment": 1, "Valeur": 1}));
        return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


    ##########################################################################################################################################
    ################################################BP_A_MBP6_CTC_DEBIT_hierarchy###############################
    #########################################################################################################################################

@api.get("/BP_A_MBP6_CTC_DEBIT/")
async def hierarchy():
     BP_A_MBP6_CTC_DEBIT_hierarchy = [

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
            ]},

    ]
     return BP_A_MBP6_CTC_DEBIT_hierarchy
    ############################################################################################################################
    ########################################BP_A_MBP6_CTC_DEBIT_HISTORIQUE#####################################################
    ##########################################################################################################################"

@api.get('/BP_A_MBP6_CTC_DEBIT_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
         if (start and end):
             a = list(BP_A_MBP6_CTC_DEBIT.find({"date": {"$gte": start, "$lte": end}},
                                                {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                                 "Type de compte": 1,
                                                 "Type": 1, "Segment": 1, "Valeur": 1}));
         else:
             a = list(BP_A_MBP6_CTC_DEBIT.find({},
                                                {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                                 "Type de compte": 1,
                                                 "Type": 1, "Segment": 1, "Valeur": 1}));
         return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
     ####################################################################################################################################################
     ######################################"BP_A_MBP6_CF_ANA_hierarchy##################################################################################
     ####################################################################################################################################################

     ################################################################
@api.get("/BP_A_MBP6_CF_ANA/")
async def hierarchy():
     BP_A_MBP6_CF_ANA_hierarchy = [



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


    ]
     return BP_A_MBP6_CF_ANA_hierarchy
     ##########################################################################################################"
     ######################################""
     ##################################################################################################################"
@api.get('/BP_A_MBP6_CF_ANA_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
         if (start and end):
             a = list(BP_A_MBP6_CF_ANA.find({"date": {"$gte": start, "$lte": end}},
                                                {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,"Type": 1,  "Valeur": 1}));
         else:
             a = list(BP_A_MBP6_CF_ANA.find({},
                                                {"_id": 0, "Date": 1, "Balance des paiements ": 1,"Cat�gorie": 1, "Type": 1,  "Valeur": 1}));
         return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

     #########################################################################################################################
     ##################################BP_A_MBP6_CF_ANE_hierarchy########################################################
     #########################################################################################################################
@api.get("/BP_A_MBP6_CF_ANE/")
async def hierarchy():
    BP_A_MBP6_CF_ANE_hierarchy = [
        {"name": "COMPTE FINANCIER",
         "elements": [
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
             {"name": "DÉRIVÉS FINANCIERS", "elements": []},
             {"name": "Autres investissements",
              "elements": [
                  {"name": "Autres participations", "elements": []},
                  {"name": "Numéraire et dépôts", "elements": []},
                  {"name": "Prêts", "elements": []},
                  {"name": "Systèmes d'assurances, de pensions et de garanties standard", "elements": []},
                  {"name": "Crédits commerciaux et avances", "elements": []},
                  {"name": "Autres comptes à recevoir/à payer", "elements": []},
              ]
              },
             {"name": "AVOIRS DE RÉSERVE", "elements": []}
         ]
         },

    ]
    return BP_A_MBP6_CF_ANE_hierarchy
#######################################################################################
##########################################BP_A_MBP6_CF_ANE_HISTORIQUE#################################################################
################################################################################################################################
@api.get('/BP_A_MBP6_CF_ANE_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
         if (start and end):
             a = list(BP_A_MBP6_CF_ANE.find({"date": {"$gte": start, "$lte": end}},
                                                {"_id": 0, "Date": 1, "Balance des paiements ": 1, "Cat�gorie": 1,"Type": 1,  "Valeur": 1}));
         else:
             a = list(BP_A_MBP6_CF_ANE.find({},
                                                {"_id": 0, "Date": 1, "Balance des paiements ": 1,"Cat�gorie": 1, "Type": 1,  "Valeur": 1}));
         return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
########################################################################################################################
########################################################################################################################
###########################################################################################################################
###########################################################################################################################
##########################################################################################################################
#####################################################################################################################
############################################################################################################################
########################################################################################################################
#############################################BP_T_MBP6_divisé par 5################################################################################
########################################################################################################################



###############################################################################################################################################################
##############################################BP_T_MBP6_CTC_SOLDE_hierrarchy#######################################"4
############################################################################################################################
@api.get("/BP_T_MBP6_CTC_SOLDE/")
async def hierarchy():
    BP_T_MBP6_CTC_SOLDE_hierarchy = [


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
            },

    ]
    return BP_T_MBP6_CTC_SOLDE_hierarchy

##############################################################################################################################
#####################################BP_T_MBP6_CTC_SOLDE_HISTORIQUE#####################################################################
#############################################################################################################################
@api.get('/BP_T_MBP6_CTC_SOLDE_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(BP_T_MBP6_CTC_SOLDE.find({"date": {"$gte": start, "$lte": end}},
                                  {"_id": 0, "Date": 1, "P�riode": 1,"Balance des paiements ": 1, "Cat�gorie": 1,"Valeur": 1}));
    else:
        a = list(BP_T_MBP6_CTC_SOLDE.find({},
                                  {"_id": 0, "Date": 1,"P�riode": 1, "Balance des paiements ": 1, "Cat�gorie": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
####################################################################################################################################################
################################################################BP_T_MBP6_CTC_CREDIT_hierarchy###############################################################################################################################################################################################


@api.get("/BP_T_MBP6_CTC_CREDIT/")
async def hierarchy():
    BP_T_MBP6_CTC_CREDIT_hierarchy = [

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
                       {"name": "Services de fabrication fournis sur des intrants physiques détenus par des tiers",
                        "elements": []},
                       {"name": "Services d’entretien et de réparation n.i.a.", "elements": []},
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
            ]},
    ]
    return BP_T_MBP6_CTC_CREDIT_hierarchy

    ############################################################################################################################
    ########################################BP_T_MBP6_CTC_CREDIT_HISTORIQUE#####################################################
    ##########################################################################################################################"
@api.get('/BP_T_MBP6_CTC_CREDIT_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
        if (start and end):
            a = list(BP_T_MBP6_CTC_CREDIT.find({"date": {"$gte": start, "$lte": end}},
                                               {"_id": 0, "Date": 1,"P�riode": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                                "Type de compte": 1,
                                                "Type": 1, "Segment": 1, "Valeur": 1}));
        else:
            a = list(BP_T_MBP6_CTC_CREDIT.find({},
                                               {"_id": 0, "Date": 1,"P�riode": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                                "Type de compte": 1,
                                                "Type": 1, "Segment": 1, "Valeur": 1}));
        return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


    ##########################################################################################################################################
    ################################################BP_T_MBP6_CTC_DEBIT_hierarchy###############################
    #########################################################################################################################################

@api.get("/BP_T_MBP6_CTC_DEBIT/")
async def hierarchy():
     BP_T_MBP6_CTC_DEBIT_hierarchy = [

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
                        {"name": "Services de fabrication fournis sur des intrants physiques détenus par des tiers",
                         "elements": []},
                        {"name": "Services d’entretien et de réparation n.i.a.", "elements": []},
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
            ]},

    ]
     return BP_T_MBP6_CTC_DEBIT_hierarchy
    ############################################################################################################################
    ########################################BP_T_MBP6_CTC_DEBIT_HISTORIQUE#####################################################
    ##########################################################################################################################"

@api.get('/BP_T_MBP6_CTC_DEBIT_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
         if (start and end):
             a = list(BP_T_MBP6_CTC_DEBIT.find({"date": {"$gte": start, "$lte": end}},
                                                {"_id": 0, "Date": 1,"P�riode": 1, "Balance des paiements ": 1, "Cat�gorie": 1,
                                                 "Type de compte": 1,
                                                 "Type": 1, "Segment": 1, "Valeur": 1}));
         else:
             a = list(BP_T_MBP6_CTC_DEBIT.find({},
                                                {"_id": 0, "Date": 1, "P�riode": 1,"Balance des paiements ": 1, "Cat�gorie": 1,
                                                 "Type de compte": 1,
                                                 "Type": 1, "Segment": 1, "Valeur": 1}));
         return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
     ####################################################################################################################################################
     ######################################"BP_T_MBP6_CF_ANA_hierarchy##################################################################################
     ####################################################################################################################################################

     ################################################################
@api.get("/BP_T_MBP6_CF_ANA/")
async def hierarchy():
     BP_T_MBP6_CF_ANA_hierarchy = [

         {"name": "COMPTE FINANCIER",
          "elements": [
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
              {"name": "DÉRIVÉS FINANCIERS", "elements": []},
              {"name": "Autres investissements",
               "elements": [
                   {"name": "Autres participations", "elements": []},
                   {"name": "Numéraire et dépôts", "elements": []},
                   {"name": "Prêts", "elements": []},
                   {"name": "Systèmes d'assurances, de pensions et de garanties standard", "elements": []},
                   {"name": "Crédits commerciaux et avances", "elements": []},

               ]
               },
              {"name": "AVOIRS DE RÉSERVE", "elements": []}
            ]
            },


    ]
     return BP_T_MBP6_CF_ANA_hierarchy
     ##########################################################################################################"
     ######################################""
     ##################################################################################################################"
@api.get('/BP_T_MBP6_CF_ANA_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
         if (start and end):
             a = list(BP_T_MBP6_CF_ANA.find({"date": {"$gte": start, "$lte": end}},
                                                {"_id": 0, "Date": 1,"P�riode": 1, "Balance des paiements ": 1, "Cat�gorie": 1,"Type": 1,  "Valeur": 1}));
         else:
             a = list(BP_T_MBP6_CF_ANA.find({},
                                                {"_id": 0, "Date": 1,"P�riode": 1, "Balance des paiements ": 1,"Cat�gorie": 1, "Type": 1,  "Valeur": 1}));
         return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

     #########################################################################################################################
     ##################################BP_T_MBP6_CF_ANE_hierarchy########################################################
     #########################################################################################################################
@api.get("/BP_T_MBP6_CF_ANE/")
async def hierarchy():
     BP_T_MBP6_CF_ANE_hierarchy = [


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
                ]},

            ]},
    ]
     return BP_T_MBP6_CF_ANE_hierarchy
################################################################################################################################
##########################################BP_T_MBP6_CF_ANE_HISTORIQUE#################################################################
################################################################################################################################
@api.get('/BP_T_MBP6_CF_ANE_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
         if (start and end):
             a = list(BP_T_MBP6_CF_ANE.find({"date": {"$gte": start, "$lte": end}},
                                                {"_id": 0, "Date": 1,"P�riode": 1, "Balance des paiements ": 1, "Cat�gorie": 1,"Type": 1,  "Valeur": 1}));
         else:
             a = list(BP_T_MBP6_CF_ANE.find({},
                                                {"_id": 0, "Date": 1,"P�riode": 1, "Balance des paiements ": 1,"Cat�gorie": 1, "Type": 1,  "Valeur": 1}));
         return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
########################################################################################################################





########################################################HCP_inflation#################################################

 
 ##############################################################################################
 ##################################""IPC_2006_hierarchy##########################################
 #############################################################################################
@api.get("/IPC_2006/")
async def hierarchy():
     IPC_2006_hierarchy = [

            {"name": "Indice des prix à la consommation 2006",
            "elements": [
                {"name": "Alimentation","elements": []},
                {"name": "Produits Non Alimentaires","elements": []},
                {"name": "Indice Général","elements": []}


            ]},

    ]
     return IPC_2006_hierarchy

#############################################################################################
#################################IPC_2006_historique#########################################
#############################################################################################
@api.get('/IPC_2006_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(IPC_2006.find({"Annee": {"$gte": start, "$lte": end}},
                                {"_id": 0, "Annee": 1, "Alimentation": 1, "Produits Non Alimentaires": 1,
                                  "Indice General": 1}));
    else:
        a = list(IPC_2006.find({}, {"_id": 0, "Annee": 1, "Alimentation": 1, "Produits Non Alimentaires": 1,
                                      "Indice General": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################
#############################IPC_2017_hierarchy###############################################
################################################################################################
@api.get("/IPC_2017/")
async def hierarchy():
     IPC_2017_hierarchy = [

            {"name": "Indice des prix à la consommation 2017",
            "elements": [
                {"name": "Alimentation", "elements": []},
                {"name": "Produits Non Alimentaires", "elements": []},
                {"name": "Indice Général", "elements": []}

            ]},

    ]
     return IPC_2017_hierarchy
#############################################################################################
#################################IPC_2017_historique#########################################
#############################################################################################

###########################################################################

############################################################################"
@api.get('/IPC_2017_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
         if (start and end):
             a = list(IPC_2017.find({"date": {"$gte": start, "$lte": end}}, {"_id": 0, "Annees": 1,"Alimentation": 1, "Produits Non Alimentaires": 1, "Indice General": 1}));
         else:
             a = list(IPC_2017.find({},{"_id": 0, "Annees": 1,"Alimentation": 1, "Produits Non Alimentaires": 1,"Indice General": 1 }));
         return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

    ################################################################################################################
###########################################Recettes_en_devises_hierarchy#########################################
###################################################################################################################
@api.get("/Recettes_en_devises/")
async def hierarchy():
    Recettes_en_devises_hierarchy=[

        {"name":"Recettes_en_devises",
        "elements":[

            ]
            },

    ]
    return Recettes_en_devises_hierarchy
################################################################################################################
###########################################Recettes_en_devises_historique#########################################
###################################################################################################################
@api.get('/Recettes_en_devises_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Recettes_en_devises.find({"Date": {"$gte": start, "$lte": end}}, {"_id": 0, "Date": 1, "Montant en MDHs": 1}));
    else:
        a = list(Recettes_en_devises.find({}, {"_id": 0, "Date": 1, "Montant en MDHs": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

    
    #######################################################################################################################################################
@api.get("/Arrivees_touristiques/")
async def hierarchy():
    Arrivees_touristiques_hierarchy=[
        {"name": "Postes frontières",
         "elements": [
             {"name": "T.AIR", "elements": []},
             {"name": "A Mohammed V", "elements": []},
             {"name": "A Agadir Almassira", "elements": []},
             {"name": "A Tanger Ibn Battouta", "elements": []},
             {"name": "A Fes-Saiss", "elements": []},
             {"name": "A Rabat-Salé", "elements": []},
             {"name": "A Laaroui", "elements": []},
             {"name": "A Oujda", "elements": []},
             {"name": "A Essaouira", "elements": []},
             {"name": "A Oaurzazate", "elements": []},
             {"name": "A Al Hoceima", "elements": []},
             {"name": "T.MER", "elements": []},
             {"name": "P Tanger Med", "elements": []},
             {"name": "P Tanger", "elements": []},
             {"name": "P Nador", "elements": []},
             {"name": "T.TERRE", "elements": []},
             {"name": "T Bab Sebta", "elements": []},
             {"name": "T Béni Anzar", "elements": []}
             



         ]
         },

        {"name":"Arrivees_touristiques ","elements":[]},

    ]
    return Arrivees_touristiques_hierarchy
################################################################################################################
###########################################Arrivees_touristiques_historique#########################################
###################################################################################################################
@api.get('/Arrivees_touristiques_HISTORIQUE')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Arrivees_touristiques.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1,"Postes frontières": 1, "Valeur": 1}));
    else:
        a = list(Arrivees_touristiques.find({}, {"_id": 0, "Date": 1,"Postes frontières": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#######################################################################################################################
################################################################################################################
###########################################arrivees_touristiques_par_nat_hierarchie#########################################
###################################################################################################################
##############################################################################################################################
@api.get("/arrivees_touristiques_par_nat/")
async def hierarchy():
    arrivees_touristiques_par_nat_hierarchy = [
        {"name": "Postes frontières",
         "elements": [
             {"name": "Touristes Etrangers", "elements": []},
             {"name": "France", "elements": []},
             {"name": "Espagne", "elements": []},
             {"name": "Royaume-Uni", "elements": []},
             {"name": "Allemagne", "elements": []},
             {"name": "Italie", "elements": []},
             {"name": "Etats Unis", "elements": []},
             {"name": "Belgique", "elements": []},
             {"name": "Hollande", "elements": []},
             {"name": "Maghreb", "elements": []},
             {"name": "Chine", "elements": []},
             {"name": "Scandinavie", "elements": []},
             {"name": "MRE", "elements": []}


         ]
         },

        {"name": "arrivees_touristiques_par_nat", "elements": []},

    ]
    return arrivees_touristiques_par_nat_hierarchy


################################################################################################################
###########################################arrivees_touristiques_par_nat_historique#########################################
###################################################################################################################
@api.get('/arrivees_touristiques_par_nat_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(arrivees_touristiques_par_nat.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Nationalit�": 1, "Valeur": 1}));
    else:
        a = list(arrivees_touristiques_par_nat.find({}, {"_id": 0, "Date": 1, "Nationalit�": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


################################################################################################################
###########################################DETTE_EXTERIEURE_PUBLIQUE_hierarchie#########################################
###################################################################################################################
##############################################################################################################################
@api.get("/DETTE_EXTERIEURE_PUBLIQUE/")
async def hierarchy():
    DETTE_EXTERIEURE_PUBLIQUE_hierarchy = [
        {"name": "DETTE_EXTERIEURE_PUBLIQUE",
         "elements": [
             {"name": "Encours de la dette extérieure publique (En millions $US)", "elements": []},
             {"name": "Encours de la dette extérieure publique (En millions DH)", "elements": []},
             {"name": "En %  du PIB", "elements": []},
             {"name": "Service de la dette (En millions $US)", "elements": []},
             {"name": "Service de la dette (En millions DH)", "elements": []},
             {"name": "En % des recettes courantes", "elements": []},
             {"name": "Charges en intérêts (En millions DH)", "elements": []},
             {"name": "En %  du PIB", "elements": []},
             {"name": "Coût moyen (%)", "elements": []}

         ]
         },



    ]
    return DETTE_EXTERIEURE_PUBLIQUE_hierarchy


################################################################################################################
###########################################DETTE_EXTERIEURE_PUBLIQUE_historique#########################################
###################################################################################################################
@api.get('/DETTE_EXTERIEURE_PUBLIQUE_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(DETTE_EXTERIEURE_PUBLIQUE.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Dette exterieure publique": 1, "Valeur": 1}));
    else:
        a = list(DETTE_EXTERIEURE_PUBLIQUE.find({}, {"_id": 0, "Date": 1, "Dette exterieure publique": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

##########################################################################################################################
#############################################dette-tresor-trimestriel##################################################
#######################################################################################################################
#############################################divisé par 8 ##############################################################
########################################################################################################################

###############################################Dette_du_tresor_service_de_la_dette_hierarchy###############################
#####################################################################################################################
@api.get("/Dette_du_tresor_service_de_la_dette/")
async def hierarchy():
    Dette_du_tresor_service_de_la_dette_hierarchy = [

             {"name": "Dette_du_tresor_service_de_la_dette",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                 ]}
              ]}
       
    ]
    return Dette_du_tresor_service_de_la_dette_hierarchy
############################################################################################################################
##############################################Dette_du_tresor_service_de_la_dette_historique##################################
################################################################################################################################
@api.get('/Dette_du_tresor_service_de_la_dette_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(DETTE_DU_TRESOR_SERVICE_DE_LA_DETTE.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1, "Dette tresor": 1,"Valeur": 1}));
    else:
        a = list(DETTE_DU_TRESOR_SERVICE_DE_LA_DETTE.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette tresor": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE_hierarchy###############################
#####################################################################################################################
@api.get("/DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE/")
async def hierarchy():
    DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE_hierarchy = [

             {"name": "DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                 ]}
              ]}


    ]
    return DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE_hierarchy
############################################################################################################################
##############################################DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE_historique##################################
################################################################################################################################
@api.get('/DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1, "Dette tresor": 1,"Valeur": 1}));
    else:
        a = list(DETTE_DU_TRESOR_ENCOURS_DE_LA_DETTE.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette tresor": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#################################################################################################################################"
###############################################DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL_hierarchy###############################
#####################################################################################################################
@api.get("/DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL/")
async def hierarchy():
    DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL_hierarchy = [

             {"name": "DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                 ]}
              ]}


    ]
    return DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL_hierarchy
############################################################################################################################
##############################################DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL_historique##################################
################################################################################################################################
@api.get('/DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1, "Dette tresor": 1,"Valeur": 1}));
    else:
        a = list(DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette tresor": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

#################################################################################################################################"
###############################################DETTE_DU_TRESOR_CHARGES_EN_INTERETS_hierarchy###############################
#####################################################################################################################
@api.get("/DETTE_DU_TRESOR_CHARGES_EN_INTERETS/")
async def hierarchy():
    DETTE_DU_TRESOR_CHARGES_EN_INTERETS_hierarchy = [

             {"name": "DETTE_DU_TRESOR_CHARGES_EN_PRINCIPAL",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                 ]}
              ]}


    ]
    return DETTE_DU_TRESOR_CHARGES_EN_INTERETS_hierarchy
############################################################################################################################
##############################################DETTE_DU_TRESOR_CHARGES_EN_INTERETS_historique##################################
################################################################################################################################
@api.get('/DETTE_DU_TRESOR_CHARGES_EN_INTERETS_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(DETTE_DU_TRESOR_CHARGES_EN_INTERETS.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1, "Dette tresor": 1,"Valeur": 1}));
    else:
        a = list(DETTE_DU_TRESOR_CHARGES_EN_INTERETS.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette tresor": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#################################################################################################################################"
###############################################dette_des_etab_et_Eses_Services_DE_LA_DETTE_hierarchy###############################
#####################################################################################################################
@api.get("/dette_des_etab_et_Eses_Services_DE_LA_DETTE/")
async def hierarchy():
    dette_des_etab_et_Eses_Services_DE_LA_DETTE_hierarchy = [

             {"name": "dette_des_etab_et_Eses_Services_DE_LA_DETTE",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                 ]}
              ]}


    ]
    return dette_des_etab_et_Eses_Services_DE_LA_DETTE_hierarchy
############################################################################################################################
##############################################dette_des_etab_et_Eses_Services_DE_LA_DETTE_historique##################################
################################################################################################################################
@api.get('/dette_des_etab_et_Eses_Services_DE_LA_DETTE_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(dette_des_etab_et_Eses_Services_DE_LA_DETTE.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1, "Dette tresor": 1,"Valeur": 1}));
    else:
        a = list(dette_des_etab_et_Eses_Services_DE_LA_DETTE.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette tresor": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#################################################################################################################################"
###############################################dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE_hierarchy###############################
#####################################################################################################################
@api.get("/dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE/")
async def hierarchy():
    dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE_hierarchy = [

             {"name": "dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                 ]}
              ]}


    ]
    return dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE_hierarchy
############################################################################################################################
##############################################dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE_historique##################################
################################################################################################################################
@api.get('/dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1, "Dette tresor": 1,"Valeur": 1}));
    else:
        a = list(dette_des_etab_et_Eses_ENCOURS_DE_LA_DETTE.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette tresor": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
##################################################################################################################################################
#############################################################################################################################################
#################################################################################################################################"
###############################################dette_des_etab_et_Eses_charges_en_principal_hierarchy###############################
#####################################################################################################################
@api.get("/dette_des_etab_et_Eses_charges_en_principal/")
async def hierarchy():
    dette_des_etab_et_Eses_charges_en_principal_hierarchy = [

             {"name": "dette_des_etab_et_Eses_charges_en_principal",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                 ]}
              ]}


    ]
    return dette_des_etab_et_Eses_charges_en_principal_hierarchy
############################################################################################################################
##############################################dette_des_etab_et_Eses_charges_en_principal_historique##################################
################################################################################################################################
@api.get('/dette_des_etab_et_Eses_charges_en_principal_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(dette_des_etab_et_Eses_charges_en_principal.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1, "Dette tresor": 1,"Valeur": 1}));
    else:
        a = list(dette_des_etab_et_Eses_charges_en_principal.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette tresor": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
############################################################################################################################
#################################################################################################################################"
###############################################Dette_des_etab_et_Eses_charges_en_interet_hierarchy###############################
#####################################################################################################################
@api.get("/Dette_des_etab_et_Eses_charges_en_interet/")
async def hierarchy():
    Dette_des_etab_et_Eses_charges_en_interet_hierarchy = [

             {"name": "Dette_des_etab_et_Eses_charges_en_interet",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Dette intérieure", "elements": []},
                     {"name": "Dette extérieure", "elements": []}
                 ]}
              ]}


    ]
    return Dette_des_etab_et_Eses_charges_en_interet_hierarchy
############################################################################################################################
##############################################Dette_des_etab_et_Eses_charges_en_interet_historique##################################
################################################################################################################################
@api.get('/Dette_des_etab_et_Eses_charges_en_interet_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Dette_des_etab_et_Eses_charges_en_interet.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1, "Dette tresor": 1,"Valeur": 1}));
    else:
        a = list(Dette_des_etab_et_Eses_charges_en_interet.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette tresor": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################

############################################################################################################################
############################################################################################################################
#################################################################################################################################"
###############################################dette_brute_sec_bancaire_hierarchy###############################
#####################################################################################################################
@api.get("/dette_brute_sec_bancaire/")
async def hierarchy():
    dette_brute_sec_bancaire_hierarchy = [

             {"name": "dette_brute_sec_bancaire",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Instruments du marché monétaire", "elements": []},
                     {"name": "Emprunts", "elements": []},
                     {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                     {"name": "Autres engagements (dettes)", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Obligations et titres", "elements": []},
                     {"name": "Emprunts", "elements": []},
                     {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                     {"name": "Autres engagements (dettes)", "elements": []}
                 ]}
              ]}


    ]
    return dette_brute_sec_bancaire_hierarchy
############################################################################################################################
##############################################dette_brute_sec_bancaire_historique##################################
################################################################################################################################
@api.get('/dette_brute_sec_bancaire_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(dette_brute_sec_bancaire.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1,"Dette brute trimestrielle": 1,"Categorie": 1, "Type": 1,"Valeur": 1}));
    else:
        a = list(dette_brute_sec_bancaire.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette brute trimestrielle": 1,"Categorie": 1, "Type": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
############################################################################################################################
############################################################################################################################
#################################################################################################################################"
##############################################dette_brute_inves_directs_hierarchy###############################
#####################################################################################################################
@api.get("/dette_brute_inves_directs/")
async def hierarchy():
    dette_brute_inves_directs_hierarchy = [

             {"name": " Investissements Directs",
              "elements": [
                {"name": "Engagements envers les investisseurs directs","elements": []},
              ]},
             {"name": "TOTALE DE LA DETTE EXTERIEURE BRUTE","elements": []}


    ]
    return dette_brute_inves_directs_hierarchy
############################################################################################################################
##############################################dette_brute_inves_directs_historique##################################
################################################################################################################################
@api.get('/dette_brute_inves_directs_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(dette_brute_inves_directs.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1,"Dette brute trimestrielle": 1,"Valeur": 1}));
    else:
        a = list(dette_brute_inves_directs.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette brute trimestrielle": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
############################################################################################################################
############################################################################################################################
#################################################################################################################################"
###############################################dette_brute_autres_sec_hierarchy###############################
#####################################################################################################################
@api.get("/dette_brute_autres_sec/")
async def hierarchy():
    dette_brute_autres_sec_hierarchy = [

             {"name": "Autres Secteurs",
              "elements": [
                  {"name": "Dette des établissements publics et dette garantie par l'Etat",
                   "elements": [

                       {"name": "Court terme",
                     "elements": [

                        {"name": "Instruments du marché monétaire", "elements": []},
                        {"name": "Emprunts", "elements": []},
                        {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                        {"name": "Autres engagements (dettes)", "elements": []}
                    ]}
                   ]},
                  {"name": "Dette des établissements publics et dette garantie par l'Etat",
                  "elements": [

                    {"name": "Moyen et long terme",
                    "elements": [
                        {"name": "Obligations et titres", "elements": []},
                        {"name": "Emprunts", "elements": []},
                        {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                        {"name": "Autres engagements (dettes)", "elements": []}
                    ]}
                  ]},
              ]}


    ]
    return dette_brute_autres_sec_hierarchy
############################################################################################################################
##############################################dette_brute_autres_sec_historique##################################
################################################################################################################################
@api.get('/dette_brute_autres_sec_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(dette_brute_autres_sec.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1,"Dette brute trimestrielle": 1,"Categorie": 1, "Type": 1,"Valeur": 1}));
    else:
        a = list(dette_brute_autres_sec.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette brute trimestrielle": 1,"Categorie": 1,"Segment": 1, "Type": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
############################################################################################################################
#################################################################################################################################"
###############################################dette_brute_autorites_mon_hierarchy###############################
#####################################################################################################################
@api.get("/dette_brute_autorites_mon/")
async def hierarchy():
    dette_brute_autorites_mon_hierarchy = [

             {"name": "dette_brute_autorites_mon",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Instruments du marché monétaire", "elements": []},
                     {"name": "Emprunts", "elements": []},
                     {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                     {"name": "Autres engagements (dettes)", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Obligations et titres", "elements": []},
                     {"name": "Emprunts", "elements": []},
                     {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                     {"name": "Autres engagements (dettes)", "elements": []}
                 ]}
              ]}


    ]
    return dette_brute_autorites_mon_hierarchy
############################################################################################################################
##############################################dette_brute_autorites_mon_historique##################################
################################################################################################################################
@api.get('/dette_brute_autorites_mon_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(dette_brute_autorites_mon.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1,"Dette brute trimestrielle": 1,"Categorie": 1, "Type": 1,"Valeur": 1}));
    else:
        a = list(dette_brute_autorites_mon.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette brute trimestrielle": 1,"Categorie": 1, "Type": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
############################################################################################################################
#################################################################################################################################"
###############################################dette_brute_administration_hierarchy###############################
#####################################################################################################################
@api.get("/dette_brute_administration/")
async def hierarchy():
    dette_brute_administration_hierarchy = [

             {"name": "dette_brute_administration",
              "elements": [
                {"name": "Court terme",
                 "elements": [

                     {"name": "Instruments du marché monétaire", "elements": []},
                     {"name": "Emprunts", "elements": []},
                     {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                     {"name": "Autres engagements (dettes)", "elements": []}
                ]},

                 {"name": "Moyen et long terme",
                 "elements": [
                     {"name": "Obligations et titres", "elements": []},
                     {"name": "Emprunts", "elements": []},
                     {"name": "Monnaie fiduciaire et dépôts", "elements": []},
                     {"name": "Autres engagements (dettes)", "elements": []}
                 ]}
              ]}


    ]
    return dette_brute_administration_hierarchy
############################################################################################################################
##############################################dette_brute_autorites_mon_historique##################################
################################################################################################################################
@api.get('/dette_brute_administration_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(dette_brute_administration.find({"Date": {"$gte": start, "$lte": end}},
                                            {"_id": 0, "Date": 1, "Periode": 1,"Dette brute trimestrielle": 1,"Categorie": 1, "Type": 1,"Valeur": 1}));
    else:
        a = list(dette_brute_administration.find({}, {"_id": 0, "Date": 1, "Periode": 1,"Dette brute trimestrielle": 1,"Categorie": 1, "Type": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))


########################################################################################################################
######################################""PIB_prix_courants_hierarchy########################################################
#######################################################################################################################
@api.get("/PIB_prix_courants/")
async def hierarchy():
    PIB_prix_courants_hierarchy=[

        {"name":"PIB_prix_courants",
        "elements":[

            ]
            },

    ]
    return PIB_prix_courants_hierarchy
########################################################################################################################
##############################PIB_prix_courants_historique##################################################################

@api.get('/PIB_prix_courants_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(PIB_prix_courants.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(PIB_prix_courants.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#######################################################################################################################""
########################################################################################################################
######################################""PIB_prix_constants_hierarchy########################################################
#######################################################################################################################
@api.get("/PIB_prix_constants/")
async def hierarchy():
    PIB_prix_constants_hierarchy=[

        {"name":"PIB_prix_constants",
        "elements":[

            ]
            },

    ]
    return PIB_prix_constants_hierarchy
########################################################################################################################
##############################PIB_prix_constants_historique##################################################################

@api.get('/PIB_prix_constants_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(PIB_prix_constants.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(PIB_prix_constants.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#######################################################################################################################""
#######################################################################################################################""
########################################################################################################################
######################################"PIB_approche_revenu_hierarchy########################################################
#######################################################################################################################
@api.get("/PIB_approche_revenu/")
async def hierarchy():
    PIB_approche_revenu_hierarchy=[

        {"name":"PIB_approche_revenu",
        "elements":[

            ]
            },

    ]
    return PIB_approche_revenu_hierarchy
########################################################################################################################
##############################PIB_approche_revenu_historique##################################################################

@api.get('/PIB_approche_revenu_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(PIB_approche_revenu.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(PIB_approche_revenu.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#######################################################################################################################""
#########################################################################################################################################################"
######################################################Agriculture#########################################################################################
########################################################################################################################################################
#######################################################################################################################""
############################################################################################################################
##############################################Production_d_agrumes_hierarchy##################################
###############################################################################################################################
@api.get("/Production_d_agrumes/")
async def hierarchy():
    Production_d_agrumes_hierarchy=[

        {"name":"Production d'agrumes",
        "elements":[

            ]
            },

    ]
    return Production_d_agrumes_hierarchy
############################################################################################################################
##############################################Production_d_agrumes_historique##################################
###############################################################################################################################
@api.get('/Production_d_agrumes_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_d_agrumes.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en Tonne": 1}));
    else:
        a = list(Production_d_agrumes.find({}, {"_id": 0, "Date": 1, "Valeur en Tonne": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#################################################################################################################################
#######################################################################################################################""
############################################################################################################################
##############################################Production_d_oeufs_hierarchy##################################
###############################################################################################################################
@api.get("/Production_d_oeufs/")
async def hierarchy():
    Production_d_oeufs_hierarchy=[

        {"name":"Production d'oeufs",
        "elements":[

            ]
            },

    ]
    return Production_d_oeufs_hierarchy
############################################################################################################################
##############################################Production_d_oeufs_historique##################################
###############################################################################################################################
@api.get('/Production_d_oeufs_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_d_agrumes.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en Tonne": 1}));
    else:
        a = list(Production_d_agrumes.find({}, {"_id": 0, "Date": 1, "Valeur en Tonne": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#################################################################################################################################
#################################################################################################################################
#######################################################################################################################""
############################################################################################################################
##############################################Production_de_bois_d_oeuvre_hierarchy##################################
###############################################################################################################################
@api.get("/Production_de_bois_d_oeuvre/")
async def hierarchy():
    Production_de_bois_d_oeuvre_hierarchy=[

        {"name":"Production de bois d'oeuvre (M**3)",
        "elements":[

            ]
            },

    ]
    return Production_de_bois_d_oeuvre_hierarchy
############################################################################################################################
##############################################Production_de_bois_d_oeuvre_historique##################################
###############################################################################################################################
@api.get('/Production_de_bois_d_oeuvre_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_de_bois_d_oeuvre.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Production_de_bois_d_oeuvre.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#################################################################################################################################
#################################################################################################################################
#######################################################################################################################""
############################################################################################################################
##############################################Production_de_bois_de_feu_hierarchy##################################
###############################################################################################################################
@api.get("/Production_de_bois_de_feu/")
async def hierarchy():
    Production_de_bois_de_feu_hierarchy=[

        {"name":"Production de bois de feu",
        "elements":[

            ]
            },

    ]
    return Production_de_bois_de_feu_hierarchy
############################################################################################################################
##############################################Production_de_bois_de_feu_historique##################################
###############################################################################################################################
@api.get('/Production_de_bois_de_feu_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_de_bois_de_feu.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Production de bois de feu (STERE(BOIS)=500KG ENV)": 1}));
    else:
        a = list(Production_de_bois_de_feu.find({}, {"_id": 0, "Date": 1, "Production de bois de feu (STERE(BOIS)=500KG ENV)": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#################################################################################################################################
#######################################################################################################################""
############################################################################################################################
##############################################Production_de_bois_industriel_hierarchy##################################
###############################################################################################################################
@api.get("/Production_de_bois_industriel/")
async def hierarchy():
    Production_de_bois_industriel_hierarchy=[

        {"name":"Production de bois industriel",
        "elements":[

            ]
            },

    ]
    return Production_de_bois_industriel_hierarchy
############################################################################################################################
##############################################Production_de_bois_industriel_historique##################################
###############################################################################################################################
@api.get('/Production_de_bois_industriel_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_de_bois_industriel.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Production_de_bois_industriel.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#################################################################################################################################
#######################################################################################################################""
############################################################################################################################
##############################################Production_de_la_viande_blanche_hierarchy##################################
###############################################################################################################################
@api.get("/Production_de_la_viande_blanche/")
async def hierarchy():
    Production_de_la_viande_blanche_hierarchy=[

        {"name":"Production de la viande blanche",
        "elements":[

            ]
            },

    ]
    return Production_de_la_viande_blanche_hierarchy
############################################################################################################################
##############################################Production_de_la_viande_blanche_historique##################################
###############################################################################################################################
@api.get('/Production_de_la_viande_blanche_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_de_la_viande_blanche.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIERS DE TONNES": 1}));
    else:
        a = list(Production_de_la_viande_blanche.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIERS DE TONNES": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
#################################################################################################################################

######################################################################################################################""
############################################################################################################################
##############################################Production_de_la_viande_rouge_hierarchy##################################
###############################################################################################################################
@api.get("/Production_de_la_viande_rouge/")
async def hierarchy():
    Production_de_la_viande_rouge_hierarchy=[

        {"name":"Production de la viande rouge",
        "elements":[

            ]
            },

    ]
    return Production_de_la_viande_rouge_hierarchy
############################################################################################################################
##############################################Production_de_la_viande_rouge_historique##################################
###############################################################################################################################
@api.get('/Production_de_la_viande_rouge_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_de_la_viande_rouge.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIERS DE TONNES": 1}));
    else:
        a = list(Production_de_la_viande_blanche.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIERS DE TONNES": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
######################################################################################################################""
############################################################################################################################
##############################################Production_de_legumineuses_hierarchy##################################
###############################################################################################################################
@api.get("/Production_de_legumineuses/")
async def hierarchy():
    Production_de_legumineuses_hierarchy=[

        {"name":"Superficie cultivée des légumineuses",
        "elements":[

            ]
            },

    ]
    return Production_de_legumineuses_hierarchy
############################################################################################################################
##############################################Production_de_legumineuses_historique##################################
###############################################################################################################################
@api.get('/Production_de_legumineuses_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_de_legumineuses.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIERS DE QUINTAUX": 1}));
    else:
        a = list(Production_de_legumineuses.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIERS DE QUINTAUX": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Superficie_cultivee_des_cultures_fourrageres_hierarchy##################################
###############################################################################################################################
@api.get("/Superficie_cultivee_des_cultures_fourrageres/")
async def hierarchy():
    Superficie_cultivee_des_cultures_fourrageres_hierarchy=[

        {"name":"Superficie cultivée des cultures fourragères",
        "elements":[

            ]
            },

    ]
    return Superficie_cultivee_des_cultures_fourrageres_hierarchy
############################################################################################################################
##############################################Superficie_cultivee_des_cultures_fourrageres_historique##################################
###############################################################################################################################
@api.get('/Superficie_cultivee_des_cultures_fourrageres_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Superficie_cultivee_des_cultures_fourrageres.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en Millers de HA": 1}));
    else:
        a = list(Superficie_cultivee_des_cultures_fourrageres.find({}, {"_id": 0, "Date": 1, "Valeur en Millers de HA": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Superficie_laissee_en_jachere_hierarchy##################################
###############################################################################################################################
@api.get("/Superficie_laissee_en_jachere/")
async def hierarchy():
    Superficie_laissee_en_jachere_hierarchy=[

        {"name":"Superficie laissée en jachère",
        "elements":[

            ]
            },

    ]
    return Superficie_laissee_en_jachere_hierarchy
############################################################################################################################
##############################################Superficie_laissee_en_jachere_historique##################################
###############################################################################################################################
@api.get('/Superficie_laissee_en_jachere_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Superficie_laissee_en_jachere.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en Millers de HA": 1}));
    else:
        a = list(Superficie_laissee_en_jachere.find({}, {"_id": 0, "Date": 1, "Valeur en Millers de HA": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
##############################################superficie_cultivee_des_cereales_hierarchy##################################
###############################################################################################################################
@api.get("/superficie_cultivee_des_cereales/")
async def hierarchy():
    superficie_cultivee_des_cereales_hierarchy=[

        {"name":"superficie cultivée des céréales",
        "elements":[

            ]
            },

    ]
    return superficie_cultivee_des_cereales_hierarchy
############################################################################################################################
##############################################superficie_cultivee_des_cereales_historique##################################
###############################################################################################################################
@api.get('/superficie_cultivee_des_cereales_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(superficie_cultivee_des_cereales.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en Millers de HA": 1}));
    else:
        a = list(superficie_cultivee_des_cereales.find({}, {"_id": 0, "Date": 1, "Valeur en Millers de HA": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
################################################################################################################################
################################################################################################################################
############################################Enseignement###############################################################
#######################################################################################################################
#######################################################################################################################
###############################################################################################################################
############################################################################################################################
##############################################NB_DE_CLASSES_hierarchy##################################
###############################################################################################################################
@api.get("/NB_DE_CLASSES/")
async def hierarchy():
    NB_DE_CLASSES_hierarchy=[

        {"name":"NB_DE_CLASSES",
        "elements":[

            ]
            },

    ]
    return NB_DE_CLASSES_hierarchy
############################################################################################################################
##############################################NB_DE_CLASSES_historique##################################
###############################################################################################################################
@api.get('/NB_DE_CLASSES_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(NB_DE_CLASSES.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(NB_DE_CLASSES.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
##########################################################################################################################
############################################################################################################################
##############################################ELEVES_DES_ECOLES_CORANIQUES_hierarchy##################################
###############################################################################################################################
@api.get("/ELEVES_DES_ECOLES_CORANIQUES/")
async def hierarchy():
    ELEVES_DES_ECOLES_CORANIQUES_hierarchy=[

        {"name":"ELEVES_DES_ECOLES_CORANIQUES",
        "elements":[

            ]
            },

    ]
    return ELEVES_DES_ECOLES_CORANIQUES_hierarchy
############################################################################################################################
##############################################ELEVES_DES_ECOLES_CORANIQUES_historique##################################
###############################################################################################################################
@api.get('/ELEVES_DES_ECOLES_CORANIQUES_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(ELEVES_DES_ECOLES_CORANIQUES.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(ELEVES_DES_ECOLES_CORANIQUES.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
##########################################################################################################################
############################################################################################################################
##############################################Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public_hierarchy##################################
###############################################################################################################################
@api.get("/Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public/")
async def hierarchy():
    Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public_hierarchy=[

        {"name":"Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public",
        "elements":[

            ]
            },

    ]
    return Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public_hierarchy
############################################################################################################################
##############################################Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public_historique##################################
###############################################################################################################################
@api.get('/Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Effectif_nouveaux_inscrits_premiere_annee_de_enseignement_primaire_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

############################################################################################################################
##############################################NB_DE_CLASSES_EC_hierarchy##################################
###############################################################################################################################
@api.get("/NB_DE_CLASSES_EC/")
async def hierarchy():
    NB_DE_CLASSES_EC_hierarchy=[

        {"name":"NB_DE_CLASSES_EC",
        "elements":[

            ]
            },

    ]
    return NB_DE_CLASSES_EC_hierarchy
############################################################################################################################
##############################################NB_DE_CLASSES_EC_historique##################################
###############################################################################################################################
@api.get('/NB_DE_CLASSES_EC_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(NB_DE_CLASSES_EC.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(NB_DE_CLASSES_EC.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_classe_enseignement_primaire_public_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_classe_enseignement_primaire_public/")
async def hierarchy():
    Nombre_classe_enseignement_primaire_public_hierarchy=[

        {"name":"Nombre_classe_enseignement_primaire_public",
        "elements":[

            ]
            },

    ]
    return Nombre_classe_enseignement_primaire_public_hierarchy
############################################################################################################################
##############################################Nombre_classe_enseignement_primaire_public_historique##################################
###############################################################################################################################
@api.get('/Nombre_classe_enseignement_primaire_public_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_classe_enseignement_primaire_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_classe_enseignement_primaire_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_de_classe_du_secondaire_collegial_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_de_classe_du_secondaire_collegial/")
async def hierarchy():
    Nombre_de_classe_du_secondaire_collegial_hierarchy=[

        {"name":"Nombre_de_classe_du_secondaire_collegial",
        "elements":[

            ]
            },

    ]
    return Nombre_de_classe_du_secondaire_collegial_hierarchy
############################################################################################################################
##############################################Nombre_de_classe_du_secondaire_collegial_historique##################################
###############################################################################################################################
@api.get('/Nombre_de_classe_du_secondaire_collegial_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_de_classe_du_secondaire_collegial.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_de_classe_du_secondaire_collegial.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_de_classes_de_enseignement_secondaire_qualifiant_public_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_de_classes_de_enseignement_secondaire_qualifiant_public/")
async def hierarchy():
    Nombre_de_classes_de_enseignement_secondaire_qualifiant_public_hierarchy=[

        {"name":"Nombre_de_classes_de_enseignement_secondaire_qualifiant_public",
        "elements":[

            ]
            },

    ]
    return Nombre_de_classes_de_enseignement_secondaire_qualifiant_public_hierarchy
############################################################################################################################
##############################################Nombre_de_classes_de_enseignement_secondaire_qualifiant_public_historique##################################
###############################################################################################################################
@api.get('/Nombre_de_classes_de_enseignement_secondaire_qualifiant_public_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_de_classes_de_enseignement_secondaire_qualifiant_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_de_classes_de_enseignement_secondaire_qualifiant_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_de_colleges_annexes_du_secondaire_collegial_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_de_colleges_annexes_du_secondaire_collegial/")
async def hierarchy():
    Nombre_de_colleges_annexes_du_secondaire_collegial_hierarchy=[

        {"name":"Nombre_de_colleges_annexes_du_secondaire_collegial",
        "elements":[

            ]
            },

    ]
    return Nombre_de_colleges_annexes_du_secondaire_collegial_hierarchy
############################################################################################################################
##############################################Nombre_de_colleges_annexes_du_secondaire_collegial_historique##################################
###############################################################################################################################
@api.get('/Nombre_de_colleges_annexes_du_secondaire_collegial_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_de_colleges_annexes_du_secondaire_collegial.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_de_colleges_annexes_du_secondaire_collegial.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_de_colleges_du_secondaire_collegial_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_de_colleges_du_secondaire_collegial/")
async def hierarchy():
    Nombre_de_colleges_du_secondaire_collegial_hierarchy=[

        {"name":"Nombre_de_colleges_du_secondaire_collegial",
        "elements":[

            ]
            },

    ]
    return Nombre_de_colleges_du_secondaire_collegial_hierarchy
############################################################################################################################
##############################################Nombre_de_colleges_du_secondaire_collegial_historique##################################
###############################################################################################################################
@api.get('/Nombre_de_colleges_du_secondaire_collegial_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_de_colleges_du_secondaire_collegial.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_de_colleges_du_secondaire_collegial.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_de_salles_utilisees_du_secondaire_collegial_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_de_salles_utilisees_du_secondaire_collegial/")
async def hierarchy():
    Nombre_de_salles_utilisees_du_secondaire_collegial_hierarchy=[

        {"name":"Nombre_de_salles_utilisees_du_secondaire_collegial",
        "elements":[

            ]
            },

    ]
    return Nombre_de_salles_utilisees_du_secondaire_collegial_hierarchy
############################################################################################################################
##############################################Nombre_de_salles_utilisees_du_secondaire_collegial_historique##################################
###############################################################################################################################
@api.get('/Nombre_de_salles_utilisees_du_secondaire_collegial_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_de_salles_utilisees_du_secondaire_collegial.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_de_salles_utilisees_du_secondaire_collegial.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_ecoles_autonomes_primaire_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_ecoles_autonomes_primaire/")
async def hierarchy():
    Nombre_ecoles_autonomes_primaire_hierarchy=[

        {"name":"Nombre_ecoles_autonomes_primaire",
        "elements":[

            ]
            },

    ]
    return Nombre_ecoles_autonomes_primaire_hierarchy
############################################################################################################################
##############################################Nombre_ecoles_autonomes_primaire_historique##################################
###############################################################################################################################
@api.get('/Nombre_ecoles_autonomes_primaire_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_ecoles_autonomes_primaire.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_ecoles_autonomes_primaire.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_eleve_enseignement_secondaire_qualifiant_prive_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_eleve_enseignement_secondaire_qualifiant_prive/")
async def hierarchy():
    Nombre_eleve_enseignement_secondaire_qualifiant_prive_hierarchy=[

        {"name":"Nombre_eleve_enseignement_secondaire_qualifiant_prive",
        "elements":[

            ]
            },

    ]
    return Nombre_eleve_enseignement_secondaire_qualifiant_prive_hierarchy
############################################################################################################################
##############################################Nombre_eleve_enseignement_secondaire_qualifiant_prive_historique##################################
###############################################################################################################################
@api.get('/Nombre_eleve_enseignement_secondaire_qualifiant_prive_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_eleve_enseignement_secondaire_qualifiant_prive.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_eleve_enseignement_secondaire_qualifiant_prive.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_eleve_enseignement_secondaire_qualifiant_public_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_eleve_enseignement_secondaire_qualifiant_public/")
async def hierarchy():
    Nombre_eleve_enseignement_secondaire_qualifiant_public_hierarchy=[

        {"name":"Nombre_eleve_enseignement_secondaire_qualifiant_public",
        "elements":[

            ]
            },

    ]
    return Nombre_eleve_enseignement_secondaire_qualifiant_public_hierarchy
############################################################################################################################
##############################################Nombre_eleve_enseignement_secondaire_qualifiant_public_historique##################################
###############################################################################################################################
@api.get('/Nombre_eleve_enseignement_secondaire_qualifiant_public_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_eleve_enseignement_secondaire_qualifiant_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_eleve_enseignement_secondaire_qualifiant_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_eleves_dans_enseignement_primaire_public_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_eleves_dans_enseignement_primaire_public/")
async def hierarchy():
    Nombre_eleves_dans_enseignement_primaire_public_hierarchy=[

        {"name":"Nombre_eleves_dans_enseignement_primaire_public",
        "elements":[

            ]
            },

    ]
    return Nombre_eleves_dans_enseignement_primaire_public_hierarchy
############################################################################################################################
##############################################Nombre_eleves_dans_enseignement_primaire_public_historique##################################
###############################################################################################################################
@api.get('/Nombre_eleves_dans_enseignement_primaire_public_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_eleves_dans_enseignement_primaire_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_eleves_dans_enseignement_primaire_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_eleves_doublant_dans_enseignement_primaire_public_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_eleves_doublant_dans_enseignement_primaire_public/")
async def hierarchy():
    Nombre_eleves_doublant_dans_enseignement_primaire_public_hierarchy=[

        {"name":"Nombre_eleves_doublant_dans_enseignement_primaire_public",
        "elements":[

            ]
            },

    ]
    return Nombre_eleves_doublant_dans_enseignement_primaire_public_hierarchy
############################################################################################################################
##############################################Nombre_eleves_doublant_dans_enseignement_primaire_public_historique##################################
###############################################################################################################################
@api.get('/Nombre_eleves_doublant_dans_enseignement_primaire_public')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_eleves_doublant_dans_enseignement_primaire_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_eleves_doublant_dans_enseignement_primaire_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_eleves_doublant_du_secondaire_collegial_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_eleves_doublant_du_secondaire_collegial/")
async def hierarchy():
    Nombre_eleves_doublant_du_secondaire_collegial_hierarchy=[

        {"name":"Nombre_eleves_doublant_du_secondaire_collegial",
        "elements":[

            ]
            },

    ]
    return Nombre_eleves_doublant_du_secondaire_collegial_hierarchy
############################################################################################################################
##############################################Nombre_eleves_doublant_du_secondaire_collegial_historique##################################
###############################################################################################################################
@api.get('/Nombre_eleves_doublant_du_secondaire_collegial')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_eleves_doublant_du_secondaire_collegial.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_eleves_doublant_du_secondaire_collegial.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_eleves_du_secondaire_collegial_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_eleves_du_secondaire_collegial/")
async def hierarchy():
    Nombre_eleves_du_secondaire_collegial_hierarchy=[

        {"name":"Nombre_eleves_du_secondaire_collegial",
        "elements":[

            ]
            },

    ]
    return Nombre_eleves_du_secondaire_collegial_hierarchy
############################################################################################################################
##############################################Nombre_eleves_du_secondaire_collegial_historique##################################
###############################################################################################################################
@api.get('/Nombre_eleves_du_secondaire_collegial')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_eleves_du_secondaire_collegial.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_eleves_du_secondaire_collegial.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_eleves_enseignement_primaire_prive_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_eleves_enseignement_primaire_prive/")
async def hierarchy():
    Nombre_eleves_enseignement_primaire_prive_hierarchy=[

        {"name":"Nombre_eleves_enseignement_primaire_prive",
        "elements":[

            ]
            },

    ]
    return Nombre_eleves_enseignement_primaire_prive_hierarchy
############################################################################################################################
##############################################Nombre_eleves_enseignement_primaire_prive_historique##################################
###############################################################################################################################
@api.get('/Nombre_eleves_enseignement_primaire_prive')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_eleves_enseignement_primaire_prive.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_eleves_enseignement_primaire_prive.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_eleves_enseignement_primaire_public_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_eleves_enseignement_primaire_public/")
async def hierarchy():
    Nombre_eleves_enseignement_primaire_public_hierarchy=[

        {"name":"Nombre_eleves_enseignement_primaire_public",
        "elements":[

            ]
            },

    ]
    return Nombre_eleves_enseignement_primaire_public_hierarchy
############################################################################################################################
##############################################Nombre_eleves_enseignement_primaire_public_historique##################################
###############################################################################################################################
@api.get('/Nombre_eleves_enseignement_primaire_public')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_eleves_enseignement_primaire_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_eleves_enseignement_primaire_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_eleves_enseignement_secondaire_collegial_prive_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_eleves_enseignement_secondaire_collegial_prive/")
async def hierarchy():
    Nombre_eleves_enseignement_secondaire_collegial_prive_hierarchy=[

        {"name":"Nombre_eleves_enseignement_secondaire_collegial_prive",
        "elements":[

            ]
            },

    ]
    return Nombre_eleves_enseignement_secondaire_collegial_prive_hierarchy
############################################################################################################################
##############################################Nombre_eleves_enseignement_secondaire_collegial_prive_historique##################################
###############################################################################################################################
@api.get('/Nombre_eleves_enseignement_secondaire_collegial_prive')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_eleves_enseignement_secondaire_collegial_prive.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_eleves_enseignement_secondaire_collegial_prive.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_enseignant_du_secondaire_collegial_prive_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_enseignant_du_secondaire_collegial_prive/")
async def hierarchy():
    Nombre_enseignant_du_secondaire_collegial_prive_hierarchy=[

        {"name":"Nombre_enseignant_du_secondaire_collegial_prive",
        "elements":[

            ]
            },

    ]
    return Nombre_enseignant_du_secondaire_collegial_prive_hierarchy
############################################################################################################################
#############################################Nombre_enseignant_du_secondaire_collegial_prive_historique##################################
###############################################################################################################################
@api.get('/Nombre_enseignant_du_secondaire_collegial_prive')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_enseignant_du_secondaire_collegial_prive.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_enseignant_du_secondaire_collegial_prive.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_etablissements_enseignement_primaire_prive_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_etablissements_enseignement_primaire_prive/")
async def hierarchy():
    Nombre_etablissements_enseignement_primaire_prive_hierarchy=[

        {"name":"Nombre_etablissements_enseignement_primaire_prive",
        "elements":[

            ]
            },

    ]
    return Nombre_etablissements_enseignement_primaire_prive_hierarchy
############################################################################################################################
#############################################Nombre_etablissements_enseignement_primaire_prive_historique##################################
###############################################################################################################################
@api.get('/Nombre_etablissements_enseignement_primaire_prive')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_etablissements_enseignement_primaire_prive.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_etablissements_enseignement_primaire_prive.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_etablissements_primaire_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_etablissements_primaire/")
async def hierarchy():
    Nombre_etablissements_primaire_hierarchy=[

        {"name":"Nombre_etablissements_primaire",
        "elements":[

            ]
            },

    ]
    return Nombre_etablissements_primaire_hierarchy
############################################################################################################################
#############################################Nombre_etablissements_primaire_historique##################################
###############################################################################################################################
@api.get('/Nombre_etablissements_primaire')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_etablissements_primaire.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_etablissements_primaire.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_formateurs_dans_les_centres_de_formation_professionnelle_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_formateurs_dans_les_centres_de_formation_professionnelle/")
async def hierarchy():
    Nombre_formateurs_dans_les_centres_de_formation_professionnelle_hierarchy=[

        {"name":"Nombre_formateurs_dans_les_centres_de_formation_professionnelle",
        "elements":[

            ]
            },

    ]
    return Nombre_formateurs_dans_les_centres_de_formation_professionnelle_hierarchy
############################################################################################################################
#############################################Nombre_formateurs_dans_les_centres_de_formation_professionnelle_historique##################################
###############################################################################################################################
@api.get('/Nombre_formateurs_dans_les_centres_de_formation_professionnelle')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_formateurs_dans_les_centres_de_formation_professionnelle.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_formateurs_dans_les_centres_de_formation_professionnelle.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_laureats_centres_formation_professionnelle_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_laureats_centres_formation_professionnelle/")
async def hierarchy():
    Nombre_laureats_centres_formation_professionnelle_hierarchy=[

        {"name":"Nombre_laureats_centres_formation_professionnelle",
        "elements":[

            ]
            },

    ]
    return Nombre_laureats_centres_formation_professionnelle_hierarchy
############################################################################################################################
#############################################Nombre_laureats_centres_formation_professionnelle_historique##################################
###############################################################################################################################
@api.get('/Nombre_laureats_centres_formation_professionnelle')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_laureats_centres_formation_professionnelle.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_laureats_centres_formation_professionnelle.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public/")
async def hierarchy():
    Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public_hierarchy=[

        {"name":"Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public",
        "elements":[

            ]
            },

    ]
    return Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public_hierarchy
############################################################################################################################
#############################################Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public_historique##################################
###############################################################################################################################
@api.get('/Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_lycees_annexes_enseignement_secondaire_qualifiant_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_lycees_enseignement_secondaire_qualifiant_public_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_lycees_enseignement_secondaire_qualifiant_public/")
async def hierarchy():
    Nombre_lycees_enseignement_secondaire_qualifiant_public_hierarchy=[

        {"name":"Nombre_lycees_enseignement_secondaire_qualifiant_public",
        "elements":[

            ]
            },

    ]
    return Nombre_lycees_enseignement_secondaire_qualifiant_public_hierarchy
############################################################################################################################
#############################################Nombre_lycees_enseignement_secondaire_qualifiant_public_historique##################################
###############################################################################################################################
@api.get('/Nombre_lycees_enseignement_secondaire_qualifiant_public')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_lycees_enseignement_secondaire_qualifiant_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_lycees_enseignement_secondaire_qualifiant_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_salles_enseignement_secondaire_qualifiant_prive_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_salles_enseignement_secondaire_qualifiant_prive/")
async def hierarchy():
    Nombre_salles_enseignement_secondaire_qualifiant_prive_hierarchy=[

        {"name":"Nombre_salles_enseignement_secondaire_qualifiant_prive",
        "elements":[

            ]
            },

    ]
    return Nombre_salles_enseignement_secondaire_qualifiant_prive_hierarchy
############################################################################################################################
#############################################Nombre_salles_enseignement_secondaire_qualifiant_prive_historique##################################
###############################################################################################################################
@api.get('/Nombre_salles_enseignement_secondaire_qualifiant_prive')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_salles_enseignement_secondaire_qualifiant_prive.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_salles_enseignement_secondaire_qualifiant_prive.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
##############################################Nombre_salles_utilisees_enseignement_primaire_public_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_salles_utilisees_enseignement_primaire_public/")
async def hierarchy():
    Nombre_salles_utilisees_enseignement_primaire_public_hierarchy=[

        {"name":"Nombre_salles_utilisees_enseignement_primaire_public",
        "elements":[

            ]
            },

    ]
    return Nombre_salles_utilisees_enseignement_primaire_public_hierarchy
############################################################################################################################
#############################################Nombre_salles_utilisees_enseignement_primaire_public_historique##################################
###############################################################################################################################
@api.get('/Nombre_salles_utilisees_enseignement_primaire_public')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_salles_utilisees_enseignement_primaire_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_salles_utilisees_enseignement_primaire_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Nombre_salles_utilisees_enseignement_secondaire_qualifiant_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_salles_utilisees_enseignement_secondaire_qualifiant/")
async def hierarchy():
    Nombre_salles_utilisees_enseignement_secondaire_qualifiant_hierarchy=[

        {"name":"Nombre_salles_utilisees_enseignement_secondaire_qualifiant",
        "elements":[

            ]
            },

    ]
    return Nombre_salles_utilisees_enseignement_secondaire_qualifiant_hierarchy
############################################################################################################################
#############################################Nombre_salles_utilisees_enseignement_secondaire_qualifiant_historique##################################
###############################################################################################################################
@api.get('/Nombre_salles_utilisees_enseignement_secondaire_qualifiant')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_salles_utilisees_enseignement_secondaire_qualifiant.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_salles_utilisees_enseignement_secondaire_qualifiant.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Nombre_satellites_primaire_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_satellites_primaire/")
async def hierarchy():
    Nombre_satellites_primaire_hierarchy=[

        {"name":"Nombre_satellites_primaire",
        "elements":[

            ]
            },

    ]
    return Nombre_satellites_primaire_hierarchy
############################################################################################################################
#############################################Nombre_satellites_primaire_historique##################################
###############################################################################################################################
@api.get('/Nombre_satellites_primaire')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_satellites_primaire.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_satellites_primaire.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Nombre_secteurs_scolaires_primaire_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_secteurs_scolaires_primaire/")
async def hierarchy():
    Nombre_secteurs_scolaires_primaire_hierarchy=[

        {"name":"Nombre_secteurs_scolaires_primaire",
        "elements":[

            ]
            },

    ]
    return Nombre_secteurs_scolaires_primaire_hierarchy
############################################################################################################################
#############################################Nombre_secteurs_scolaires_primaire_historique##################################
###############################################################################################################################
@api.get('/Nombre_secteurs_scolaires_primaire')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_secteurs_scolaires_primaire.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_secteurs_scolaires_primaire.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Personnel_enseignant_de_enseignement_primaire_prive_hierarchy##################################
###############################################################################################################################
@api.get("/Personnel_enseignant_de_enseignement_primaire_prive/")
async def hierarchy():
    Personnel_enseignant_de_enseignement_primaire_prive_hierarchy=[

        {"name":"Personnel_enseignant_de_enseignement_primaire_prive",
        "elements":[

            ]
            },

    ]
    return Personnel_enseignant_de_enseignement_primaire_prive_hierarchy
############################################################################################################################
#############################################Personnel_enseignant_de_enseignement_primaire_prive_historique##################################
###############################################################################################################################
@api.get('/Personnel_enseignant_de_enseignement_primaire_prive')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Personnel_enseignant_de_enseignement_primaire_prive.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Personnel_enseignant_de_enseignement_primaire_prive.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Personnel_enseignant_de_enseignement_secondaire_collegial_public_hierarchy##################################
###############################################################################################################################
@api.get("/Personnel_enseignant_de_enseignement_secondaire_collegial_public/")
async def hierarchy():
    Personnel_enseignant_de_enseignement_secondaire_collegial_public_hierarchy=[

        {"name":"Personnel_enseignant_de_enseignement_secondaire_collegial_public",
        "elements":[

            ]
            },

    ]
    return Personnel_enseignant_de_enseignement_secondaire_collegial_public_hierarchy
############################################################################################################################
#############################################Personnel_enseignant_de_enseignement_secondaire_collegial_public_historique##################################
###############################################################################################################################
@api.get('/Personnel_enseignant_de_enseignement_secondaire_collegial_public')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Personnel_enseignant_de_enseignement_secondaire_collegial_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Personnel_enseignant_de_enseignement_secondaire_collegial_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Personnel_enseignant_enseignement_primaire_public_hierarchy##################################
###############################################################################################################################
@api.get("/Personnel_enseignant_enseignement_primaire_public/")
async def hierarchy():
    Personnel_enseignant_enseignement_primaire_public_hierarchy=[

        {"name":"Personnel_enseignant_enseignement_primaire_public",
        "elements":[

            ]
            },

    ]
    return Personnel_enseignant_enseignement_primaire_public_hierarchy
############################################################################################################################
#############################################PPersonnel_enseignant_enseignement_primaire_public_historique##################################
###############################################################################################################################
@api.get('/Personnel_enseignant_enseignement_primaire_public')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Personnel_enseignant_enseignement_primaire_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Personnel_enseignant_enseignement_primaire_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Personnel_enseignant_enseignement_secondaire_qualifiant_prive_hierarchy##################################
###############################################################################################################################
@api.get("/Personnel_enseignant_enseignement_secondaire_qualifiant_prive/")
async def hierarchy():
    Personnel_enseignant_enseignement_secondaire_qualifiant_prive_hierarchy=[

        {"name":"Personnel_enseignant_enseignement_secondaire_qualifiant_prive",
        "elements":[

            ]
            },

    ]
    return Personnel_enseignant_enseignement_secondaire_qualifiant_prive_hierarchy
############################################################################################################################
#############################################Personnel_enseignant_enseignement_secondaire_qualifiant_prive_historique##################################
###############################################################################################################################
@api.get('/Personnel_enseignant_enseignement_secondaire_qualifiant_prive')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Personnel_enseignant_enseignement_secondaire_qualifiant_prive.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Personnel_enseignant_enseignement_secondaire_qualifiant_prive.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Personnel_enseignant_enseignement_secondaire_qualifiant_public_hierarchy##################################
###############################################################################################################################
@api.get("/Personnel_enseignant_enseignement_secondaire_qualifiant_public/")
async def hierarchy():
    Personnel_enseignant_enseignement_secondaire_qualifiant_public_hierarchy=[

        {"name":"Personnel_enseignant_enseignement_secondaire_qualifiant_public",
        "elements":[

            ]
            },

    ]
    return Personnel_enseignant_enseignement_secondaire_qualifiant_public_hierarchy
############################################################################################################################
#############################################Personnel_enseignant_enseignement_secondaire_qualifiant_public_historique##################################
###############################################################################################################################
@api.get('/Personnel_enseignant_enseignement_secondaire_qualifiant_public')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Personnel_enseignant_enseignement_secondaire_qualifiant_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Personnel_enseignant_enseignement_secondaire_qualifiant_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Personnel_enseignant_enseignement_secondaire_qualifiant_public_2_hierarchy##################################
###############################################################################################################################
@api.get("/Personnel_enseignant_enseignement_secondaire_qualifiant_public_2/")
async def hierarchy():
    Personnel_enseignant_enseignement_secondaire_qualifiant_public_2_hierarchy=[

        {"name":"Personnel_enseignant_enseignement_secondaire_qualifiant_public_2",
        "elements":[

            ]
            },

    ]
    return Personnel_enseignant_enseignement_secondaire_qualifiant_public_2_hierarchy
############################################################################################################################
#############################################Personnel_enseignant_enseignement_secondaire_qualifiant_public_2_historique##################################
###############################################################################################################################
@api.get('/Personnel_enseignant_enseignement_secondaire_qualifiant_public_2')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Personnel_enseignant_enseignement_secondaire_qualifiant_public_2.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Personnel_enseignant_enseignement_secondaire_qualifiant_public_2.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################effectif_etablissement_secondaire_collegial_prive_hierarchy##################################
###############################################################################################################################
@api.get("/effectif_etablissement_secondaire_collegial_prive/")
async def hierarchy():
    effectif_etablissement_secondaire_collegial_prive_hierarchy=[

        {"name":"effectif_etablissement_secondaire_collegial_prive",
        "elements":[

            ]
            },

    ]
    return effectif_etablissement_secondaire_collegial_prive_hierarchy
############################################################################################################################
#############################################effectif_etablissement_secondaire_collegial_prive_historique##################################
###############################################################################################################################
@api.get('/effectif_etablissement_secondaire_collegial_prive')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(effectif_etablissement_secondaire_collegial_prive.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(effectif_etablissement_secondaire_collegial_prive.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################effectif_etablissement_secondaire_qualifiant_prive_hierarchy##################################
###############################################################################################################################
@api.get("/effectif_etablissement_secondaire_qualifiant_prive/")
async def hierarchy():
    effectif_etablissement_secondaire_qualifiant_prive_hierarchy=[

        {"name":"effectif_etablissement_secondaire_qualifiant_prive",
        "elements":[

            ]
            },

    ]
    return effectif_etablissement_secondaire_qualifiant_prive_hierarchy
############################################################################################################################
#############################################effectif_etablissement_secondaire_qualifiant_prive_historique##################################
###############################################################################################################################
@api.get('/effectif_etablissement_secondaire_qualifiant_prive')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(effectif_etablissement_secondaire_qualifiant_prive.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(effectif_etablissement_secondaire_qualifiant_prive.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################eleves_doublant_de_enseignement_secondaire_qualifiant_public_hierarchy##################################
###############################################################################################################################
@api.get("/eleves_doublant_de_enseignement_secondaire_qualifiant_public/")
async def hierarchy():
    eleves_doublant_de_enseignement_secondaire_qualifiant_public_hierarchy=[

        {"name":"eleves_doublant_de_enseignement_secondaire_qualifiant_public",
        "elements":[

            ]
            },

    ]
    return eleves_doublant_de_enseignement_secondaire_qualifiant_public_hierarchy
############################################################################################################################
#############################################eleves_doublant_de_enseignement_secondaire_qualifiant_public_historique##################################
###############################################################################################################################
@api.get('/eleves_doublant_de_enseignement_secondaire_qualifiant_public')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(eleves_doublant_de_enseignement_secondaire_qualifiant_public.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(eleves_doublant_de_enseignement_secondaire_qualifiant_public.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

############################################################################################################################
#############################################Taux_d_achevement_hierarchy##################################
###############################################################################################################################
@api.get("/Taux_d_achevement/")
async def hierarchy():
    Taux_d_achevement_hierarchy=[

        {"name":"Taux_d_achevement",
        "elements":[

            ]
            },

    ]
    return Taux_d_achevement_hierarchy
############################################################################################################################
#############################################Taux_d_achevement_historique##################################
###############################################################################################################################
@api.get('/Taux_d_achevement')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Taux_d_achevement.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Taux_d_achevement.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Budget_education_national_hierarchy##################################
###############################################################################################################################
@api.get("/Budget_education_national/")
async def hierarchy():
    Budget_education_national_hierarchy=[

        {"name":"Budget_education_national",
        "elements":[

            ]
            },

    ]
    return Budget_education_national_hierarchy
############################################################################################################################
#############################################Budget_education_national_historique##################################
###############################################################################################################################
@api.get('/Budget_education_national')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Budget_education_national.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Budget_education_national.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Nombre_d_etablissements_EC_hierarchy##################################
###############################################################################################################################
@api.get("/Nombre_d_etablissements_EC/")
async def hierarchy():
    Nombre_d_etablissements_EC_hierarchy=[

        {"name":"Nombre_d_etablissements_EC",
        "elements":[

            ]
            },

    ]
    return Nombre_d_etablissements_EC_hierarchy
############################################################################################################################
#############################################Nombre_d_etablissements_EC_historique##################################
###############################################################################################################################
@api.get('/Nombre_d_etablissements_EC')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_d_etablissements_EC.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Nombre_d_etablissements_EC.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
############################################################################################################################
#############################################Personnel_enseignant_EC_hierarchy##################################
###############################################################################################################################
@api.get("/Personnel_enseignant_EC/")
async def hierarchy():
    Personnel_enseignant_EC_hierarchy=[

        {"name":"Personnel_enseignant_EC",
        "elements":[

            ]
            },

    ]
    return Personnel_enseignant_EC_hierarchy
############################################################################################################################
#############################################Personnel_enseignant_EC_historique##################################
###############################################################################################################################
@api.get('/Personnel_enseignant_EC')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Personnel_enseignant_EC.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Personnel_enseignant_EC.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
###########################################################################################################################
############################################----------ENERGIE---------------#################################################
#######################################################################################################################
#######################################################################################################################
###############################################################################################################################
############################################################################################################################
##################################################Approvisionnement énergétique total hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Approvisionnement_energetique_total/")
async def hierarchy():
    Approvisionnement_energetique_total_hierarchy=[

        {"name":"Approvisionnement_energetique_total",
        "elements":[

            ]
            },

    ]
    return Approvisionnement_energetique_total_hierarchy
############################################################################################################################
#############################################Approvisionnement énergétique total_historique##################################
###############################################################################################################################
@api.get('/Approvisionnement_energetique_total_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Approvisionnement_energetique_total.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en Tonne equivalent Petrole": 1}));
    else:
        a = list(Approvisionnement_energetique_total.find({}, {"_id": 0, "Date": 1, "Valeur en Tonne equivalent Petrole": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
##################################################Consommation_energie hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Consommation_energie/")
async def hierarchy():
    Consommation_energie_hierarchy=[

        {"name":"Consommation_energie",
        "elements":[

            ]
            },

    ]
    return Consommation_energie_hierarchy
############################################################################################################################
#############################################Consommation_energie_historique##################################
###############################################################################################################################
@api.get('/Consommation_energie_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Consommation_energie.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en Tonne equivalent Petrole": 1}));
    else:
        a = list(Consommation_energie.find({}, {"_id": 0, "Date": 1, "Valeur en Tonne equivalent Petrole": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
##################################################Consommation_de_produits_petroliers hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Consommation_de_produits_petroliers/")
async def hierarchy():
    Consommation_de_produits_petroliers_hierarchy=[

        {"name":"Consommation_de_produits_petroliers",
        "elements":[

            ]
            },

    ]
    return Consommation_de_produits_petroliers_hierarchy
############################################################################################################################
#############################################Consommation_de_produits_petroliers_historique##################################
###############################################################################################################################
@api.get('/Consommation_de_produits_petroliers_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Consommation_de_produits_petroliers.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    else:
        a = list(Consommation_de_produits_petroliers.find({}, {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
##################################################Consommation_de_produits_petroliers_energetiques hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Consommation_de_produits_petroliers_energetiques/")
async def hierarchy():
    Consommation_de_produits_petroliers_energetiques_hierarchy=[

        {"name":"Consommation_de_produits_petroliers_energetiques",
        "elements":[

            ]
            },

    ]
    return Consommation_de_produits_petroliers_energetiques_hierarchy
############################################################################################################################
#############################################Consommation_de_produits_petroliers_energetiques_historique##################################
###############################################################################################################################
@api.get('/Consommation_de_produits_petroliers_energetiques_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Consommation_de_produits_petroliers_energetiques.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    else:
        a = list(Consommation_de_produits_petroliers_energetiques.find({}, {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
#################################################Consommation_de_produits_petroliers_non_energetiques hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Consommation_de_produits_petroliers_non_energetiques/")
async def hierarchy():
    Consommation_de_produits_petroliers_non_energetiques_hierarchy=[

        {"name":"Consommation_de_produits_petroliers_non_energetiques",
        "elements":[

            ]
            },

    ]
    return Consommation_de_produits_petroliers_non_energetiques_hierarchy
############################################################################################################################
#############################################Consommation_de_produits_petroliers_non_energetiques_historique##################################
###############################################################################################################################
@api.get('/Consommation_de_produits_petroliers_non_energetiques_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Consommation_de_produits_petroliers_non_energetiques.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    else:
        a = list(Consommation_de_produits_petroliers_non_energetiques.find({}, {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
#################################################Consommation_des_huiles_et_graisses_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Consommation_des_huiles_et_graisses/")
async def hierarchy():
    Consommation_des_huiles_et_graisses_hierarchy=[

        {"name":"Consommation_des_huiles_et_graisses",
        "elements":[

            ]
            },

    ]
    return Consommation_des_huiles_et_graisses_hierarchy
############################################################################################################################
#############################################Consommation_des_huiles_et_graisses_historique##################################
###############################################################################################################################
@api.get('/Consommation_des_huiles_et_graisses_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Consommation_des_huiles_et_graisses.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    else:
        a = list(Consommation_des_huiles_et_graisses.find({}, {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
#################################################Consommation_par_les_industriels_autoproducteurs_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Consommation_par_les_industriels_autoproducteurs/")
async def hierarchy():
    Consommation_par_les_industriels_autoproducteurs_hierarchy=[

        {"name":"Consommation_par_les_industriels_autoproducteurs",
        "elements":[

            ]
            },

    ]
    return Consommation_par_les_industriels_autoproducteurs_hierarchy
############################################################################################################################
#############################################Consommation_par_les_industriels_autoproducteurs_historique##################################
###############################################################################################################################
@api.get('/Consommation_par_les_industriels_autoproducteurs_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Consommation_par_les_industriels_autoproducteurs.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    else:
        a = list(Consommation_par_les_industriels_autoproducteurs.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
#################################################Consommation_par_les_petites_distributions_isolees_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Consommation_par_les_petites_distributions_isolees/")
async def hierarchy():
    Consommation_par_les_petites_distributions_isolees_hierarchy=[

        {"name":"Consommation_par_les_petites_distributions_isolees",
        "elements":[

            ]
            },

    ]
    return Consommation_par_les_petites_distributions_isolees_hierarchy
############################################################################################################################
#############################################Consommation_par_les_petites_distributions_isolees_historique##################################
###############################################################################################################################
@api.get('/Consommation_par_les_petites_distributions_isolees_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Consommation_par_les_petites_distributions_isolees.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    else:
        a = list(Consommation_par_les_petites_distributions_isolees.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
#################################################Exportation_de_charbon_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Exportation_de_charbon/")
async def hierarchy():
    Exportation_de_charbon_hierarchy=[

        {"name":"Exportation_de_charbon",
        "elements":[

            ]
            },

    ]
    return Exportation_de_charbon_hierarchy
############################################################################################################################
#############################################Exportation_de_charbon_historique##################################
###############################################################################################################################
@api.get('/Exportation_de_charbon_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Exportation_de_charbon.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date ": 1, "Valeur en MILLIERS DE TONNES": 1}));
    else:
        a = list(Exportation_de_charbon.find({}, {"_id": 0, "Date ": 1, "Valeur en MILLIERS DE TONNES": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
#################################################Exportation_de_charbon_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Exportation_de_charbon/")
async def hierarchy():
    Exportation_de_charbon_hierarchy=[

        {"name":"Exportation_de_charbon",
        "elements":[

            ]
            },

    ]
    return Exportation_de_charbon_hierarchy
############################################################################################################################
#############################################Exportation_de_charbon_historique##################################
###############################################################################################################################
@api.get('/Exportation_de_charbon_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Exportation_de_charbon.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date ": 1, "Valeur en MILLIERS DE TONNES": 1}));
    else:
        a = list(Exportation_de_charbon.find({}, {"_id": 0, "Date ": 1, "Valeur en MILLIERS DE TONNES": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
#################################################Exportation_de_Naphta_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Exportation_de_Naphta/")
async def hierarchy():
    Exportation_de_Naphta_hierarchy=[

        {"name":"Exportation_de_Naphta",
        "elements":[

            ]
            },

    ]
    return Exportation_de_Naphta_hierarchy
############################################################################################################################
#############################################Exportation_de_Naphta_historique##################################
###############################################################################################################################
@api.get('/Exportation_de_Naphta_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Exportation_de_Naphta.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    else:
        a = list(Exportation_de_Naphta.find({}, {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
#################################################Exportation_des_produits_petroliers_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Exportation_des_produits_petroliers/")
async def hierarchy():
    Exportation_des_produits_petroliers_hierarchy=[

        {"name":"Exportation_des_produits_petroliers",
        "elements":[

            ]
            },

    ]
    return Exportation_des_produits_petroliers_hierarchy
############################################################################################################################
#############################################Exportation_des_produits_petroliers_historique##################################
###############################################################################################################################
@api.get('/Exportation_des_produits_petroliers_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Exportation_des_produits_petroliers.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    else:
        a = list(Exportation_des_produits_petroliers.find({}, {"_id": 0, "Date": 1, "Valeur en TONNE": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
#################################################LoLongueur_des_lignes_de_transport_electricite_haute_tension_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Longueur_des_lignes_de_transport_electricite_haute_tension/")
async def hierarchy():
    Longueur_des_lignes_de_transport_electricite_haute_tension_hierarchy=[

        {"name":"Longueur_des_lignes_de_transport_electricite_haute_tension",
        "elements":[

            ]
            },

    ]
    return Longueur_des_lignes_de_transport_electricite_haute_tension_hierarchy
############################################################################################################################
#############################################Longueur_des_lignes_de_transport_electricite_haute_tension_historique##################################
###############################################################################################################################
@api.get('/Longueur_des_lignes_de_transport_electricite_haute_tension_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Longueur_des_lignes_de_transport_electricite_haute_tension.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en KM": 1}));
    else:
        a = list(Longueur_des_lignes_de_transport_electricite_haute_tension.find({}, {"_id": 0, "Date": 1, "Valeur en KM": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
################################################Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc/")
async def hierarchy():
    Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc_hierarchy=[

        {"name":"Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc",
        "elements":[

            ]
            },

    ]
    return Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc_hierarchy
############################################################################################################################
#############################################Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc_historique##################################
###############################################################################################################################
@api.get('/Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIERS HEURES": 1}));
    else:
        a = list(Nombre_dheures_de_travail_dans_les_Charbonnages_du_Maroc.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIERS HEURES": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
################################################Personnel_de_ONE_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Personnel_de_ONE/")
async def hierarchy():
    Personnel_de_ONE_hierarchy=[

        {"name":"Personnel_de_ONE",
        "elements":[

            ]
            },

    ]
    return Personnel_de_ONE_hierarchy
############################################################################################################################
#############################################Personnel_de_ONE_historique##################################
###############################################################################################################################
@api.get('/Personnel_de_ONE_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Personnel_de_ONE.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur": 1}));
    else:
        a = list(Personnel_de_ONE.find({}, {"_id": 0, "Date": 1, "Valeur": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

###############################################################################################################################
############################################################################################################################
################################################Production_des_apports_des_tiers_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Production_des_apports_des_tiers/")
async def hierarchy():
    Production_des_apports_des_tiers_hierarchy=[

        {"name":"Production_des_apports_des_tiers",
        "elements":[

            ]
            },

    ]
    return Production_des_apports_des_tiers_hierarchy
############################################################################################################################
############################################Production_des_apports_des_tiers_historique##################################
###############################################################################################################################
@api.get('/Production_des_apports_des_tiers_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_des_apports_des_tiers.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    else:
        a = list(Production_des_apports_des_tiers.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
################################################Production_du_parc_eolien_de_ONE_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Production_du_parc_eolien_de_ONE/")
async def hierarchy():
    Production_du_parc_eolien_de_ONE_hierarchy=[

        {"name":"Production_du_parc_eolien_de_ONE",
        "elements":[

            ]
            },

    ]
    return Production_du_parc_eolien_de_ONE_hierarchy
############################################################################################################################
############################################Production_du_parc_eolien_de_ONE_historique##################################
###############################################################################################################################
@api.get('/Production_du_parc_eolien_de_ONE_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_du_parc_eolien_de_ONE.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    else:
        a = list(Production_du_parc_eolien_de_ONE.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))

###############################################################################################################################
############################################################################################################################
################################################Production_nette_de_charbon_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Production_nette_de_charbon/")
async def hierarchy():
    Production_nette_de_charbon_hierarchy=[

        {"name":"Production_nette_de_charbon",
        "elements":[

            ]
            },

    ]
    return Production_nette_de_charbon_hierarchy
############################################################################################################################
############################################Production_nette_de_charbon_historique##################################
###############################################################################################################################
@api.get('/Production_nette_de_charbon_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_nette_de_charbon.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIERS DE TONNES": 1}));
    else:
        a = list(Production_nette_de_charbon.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIERS DE TONNES": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
################################################Production_nette_electricite_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Production_nette_electricite/")
async def hierarchy():
    Production_nette_electricite_hierarchy=[

        {"name":"Production_nette_electricite",
        "elements":[

            ]
            },

    ]
    return Production_nette_electricite_hierarchy
############################################################################################################################
############################################Production_nette_electricite_historique##################################
###############################################################################################################################
@api.get('/Production_nette_electricite_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_nette_electricite.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    else:
        a = list(Production_nette_electricite.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
################################################Production_nette_des_petites_distributions_isolees_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Production_nette_des_petites_distributions_isolees/")
async def hierarchy():
    Production_nette_des_petites_distributions_isolees_hierarchy=[

        {"name":"Production_nette_des_petites_distributions_isolees",
        "elements":[

            ]
            },

    ]
    return Production_nette_des_petites_distributions_isolees_hierarchy
############################################################################################################################
############################################Production_nette_electricite_historique##################################
###############################################################################################################################
@api.get('/Production_nette_des_petites_distributions_isolees_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_nette_des_petites_distributions_isolees.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    else:
        a = list(Production_nette_des_petites_distributions_isolees.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
##############################################Production_total_de_ONE_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Production_total_de_ONE/")
async def hierarchy():
    Production_total_de_ONE_hierarchy=[

        {"name":"Production_total_de_ONE",
        "elements":[

            ]
            },

    ]
    return Production_total_de_ONE_hierarchy
############################################################################################################################
############################################Production_nette_electricite_historique##################################
###############################################################################################################################
@api.get('/Production_total_de_ONE_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Production_total_de_ONE.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    else:
        a = list(Production_total_de_ONE.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIONS DE KWH": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
##############################################Puissance_installee_par_ONE_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Puissance_installee_par_ONE/")
async def hierarchy():
    Puissance_installee_par_ONE_hierarchy=[

        {"name":"Puissance_installee_par_ONE",
        "elements":[

            ]
            },

    ]
    return Puissance_installee_par_ONE_hierarchy
############################################################################################################################
############################################Production_nette_electricite_historique##################################
###############################################################################################################################
@api.get('/Puissance_installee_par_ONE_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Puissance_installee_par_ONE.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIONS DE WATTS": 1}));
    else:
        a = list(Puissance_installee_par_ONE.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIONS DE WATTS": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
##############################################Puissance_totale_installee au_maroc_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Puissance_totale_installee_au_maroc/")
async def hierarchy():
    Puissance_totale_installee_au_maroc_hierarchy=[

        {"name":"Puissance_totale_installee_au_maroc",
        "elements":[

            ]
            },

    ]
    return Puissance_totale_installee_au_maroc_hierarchy
############################################################################################################################
############################################Puissance_totale_installee_au_maroc_historique##################################
###############################################################################################################################
@api.get('/Puissance_totale_installee_au_maroc_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Puissance_totale_installee_au_maroc.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIONS DE WATTS": 1}));
    else:
        a = list(Puissance_totale_installee_au_maroc.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIONS DE WATTS": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))
###############################################################################################################################
############################################################################################################################
#############################################Ventes_locales_de_charbon_hierarchy###############################################
###############################################################################################################################
############################################################################################################################
@api.get("/Ventes_locales_de_charbon/")
async def hierarchy():
    Ventes_locales_de_charbon_hierarchy=[

        {"name":"Ventes_locales_de_charbon",
        "elements":[

            ]
            },

    ]
    return Ventes_locales_de_charbon_hierarchy
############################################################################################################################
############################################Ventes_locales_de_charbon_historique##################################
###############################################################################################################################
@api.get('/Ventes_locales_de_charbon_historique')
def getComptes(start: int = 0, end: int = 0):
    if (start and end):
        a = list(Ventes_locales_de_charbon.find({"Date": {"$gte": start, "$lte": end}},
                                     {"_id": 0, "Date": 1, "Valeur en MILLIERS DE TONNES": 1}));
    else:
        a = list(Ventes_locales_de_charbon.find({}, {"_id": 0, "Date": 1, "Valeur en MILLIERS DE TONNES": 1}));
    return JSONResponse(status_code=200, content=json.loads(json_util.dumps(a)))





