# Documentação Detector de Recalls

Primeiro passo: a organização e estrutura do projeto escolhida foi-se baseada no conceito Cookiecutter;
Segundo passo: foi-se criado um script para transformar o dataset no formato ".txt" para o formato ".csv";
Terceiro passo: foi-se filtrado e eliminado os dados antes de 2014 no primeiro dataset, de modo que apenas os dados de 2014 a 2024 foram selecionados para análise e treino;
Quarto passo: foi-se mesclado os três datasets para melhor análise e desenvolvimento do modelo preditivo;

## Descrição das Features

FIELDS:
=======

Field#  Name              Type/Size     Description
------  ---------         ---------     --------------------------------------
1       CMPLID            CHAR(9)       NHTSA'S INTERNAL UNIQUE SEQUENCE NUMBER.
                                        IS AN UPDATEABLE FIELD,THUS DATA FOR A
                                        GIVEN RECORD POTENTIALLY COULD CHANGE FROM
                                        ONE DATA OUTPUT FILE TO THE NEXT.
2       ODINO             CHAR(9)       NHTSA'S INTERNAL REFERENCE NUMBER.
                                        THIS NUMBER MAY BE REPEATED FOR
                                        MULTIPLE COMPONENTS.
                                        ALSO, IF LDATE IS PRIOR TO DEC 15, 2002,
                                        THIS NUMBER MAY BE REPEATED FOR MULTIPLE
                                        PRODUCTS OWNED BY THE SAME COMPLAINANT.
3       MFR_NAME          CHAR(40)      MANUFACTURER'S NAME
4       MAKETXT           CHAR(25)      VEHICLE/EQUIPMENT MAKE
5       MODELTXT          CHAR(256)     VEHICLE/EQUIPMENT MODEL
6       YEARTXT           CHAR(4)       MODEL YEAR, 9999 IF UNKNOWN or N/A
7       CRASH             CHAR(1)       WAS VEHICLE INVOLVED IN A CRASH, 'Y' OR 'N'
8       FAILDATE          CHAR(8)       DATE OF INCIDENT (YYYYMMDD)
9       FIRE              CHAR(1)       WAS VEHICLE INVOLVED IN A FIRE 'Y' OR 'N'
10      INJURED           NUMBER(2)     NUMBER OF PERSONS INJURED
11      DEATHS            NUMBER(2)     NUMBER OF FATALITIES
12      COMPDESC          CHAR(128)     SPECIFIC COMPONENT'S DESCRIPTION
13      CITY              CHAR(30)      CONSUMER'S CITY
14      STATE             CHAR(2)       CONSUMER'S STATE CODE
15      VIN               CHAR(11)      VEHICLE'S VIN#
16      DATEA             CHAR(8)       DATE ADDED TO FILE (YYYYMMDD)
17      LDATE             CHAR(8)       DATE COMPLAINT RECEIVED BY NHTSA (YYYYMMDD)
18      MILES             NUMBER(7)     VEHICLE MILEAGE AT FAILURE
19      OCCURENCES        NUMBER(4)     NUMBER OF OCCURRENCES
20      CDESCR            CHAR(2048)    DESCRIPTION OF THE COMPLAINT
21      CMPL_TYPE         CHAR(4)       SOURCE OF COMPLAINT CODE:
                                          CAG  =CONSUMER ACTION GROUP
                                          CON  =FORWARDED FROM A CONGRESSIONAL OFFICE
                                          DP   =DEFECT PETITION,RESULT OF A DEFECT PETITION
                                          EVOQ =HOTLINE VOQ
                                          EWR  =EARLY WARNING REPORTING
                                          INS  =INSURANCE COMPANY
                                          IVOQ =NHTSA WEB SITE
                                          LETR =CONSUMER LETTER
                                          MAVQ =NHTSA MOBILE APP
                                          MIVQ =NHTSA MOBILE APP
                                          MVOQ =OPTICAL MARKED VOQ
                                          RC   =RECALL COMPLAINT,RESULT OF A RECALL INVESTIGATION
                                          RP   =RECALL PETITION,RESULT OF A RECALL PETITION
                                          SVOQ =PORTABLE SAFETY COMPLAINT FORM (PDF)
                                          VOQ  =NHTSA VEHICLE OWNERS QUESTIONNAIRE
22      POLICE_RPT_YN     CHAR(1)       WAS INCIDENT REPORTED TO POLICE 'Y' OR 'N'
23      PURCH_DT          CHAR(8)       DATE PURCHASED (YYYYMMDD)
24      ORIG_OWNER_YN     CHAR(1)       WAS ORIGINAL OWNER 'Y' OR 'N'
25      ANTI_BRAKES_YN    CHAR(1)       ANTI-LOCK BRAKES 'Y' OR 'N'
26      CRUISE_CONT_YN    CHAR(1)       CRUISE CONTROL 'Y' OR 'N'
27      NUM_CYLS          NUMBER(2)     NUMBER OF CYLINDERS
28      DRIVE_TRAIN       CHAR(4)       DRIVE TRAIN TYPE [AWD,4WD,FWD,RWD]
29      FUEL_SYS          CHAR(4)       FUEL SYSTEM CODE:
                                           FI =FUEL INJECTION
                                           TB =TURBO
30      FUEL_TYPE         CHAR(4)       FUEL TYPE CODE:
                                           BF =BIFUEL
                                           CN =CNG/LPG
                                           DS =DIESEL
                                           GS =GAS
                                           HE =HYBRID ELECTRIC
31      TRANS_TYPE        CHAR(4)       VEHICLE TRANSMISSION TYPE [AUTO, MAN]
32      VEH_SPEED         NUMBER(3)     VEHICLE SPEED
33      DOT               CHAR(20)      DEPARTMENT OF TRANSPORTATION TIRE IDENTIFIER
34      TIRE_SIZE         CHAR(30)      TIRE SIZE
35      LOC_OF_TIRE       CHAR(4)       LOCATION OF TIRE CODE:
                                           FSW =DRIVER SIDE FRONT
                                           DSR =DRIVER SIDE REAR
                                           FTR =PASSENGER SIDE FRONT
                                           PSR =PASSENGER SIDE REAR
                                           SPR =SPARE
36      TIRE_FAIL_TYPE    CHAR(4)       TYPE OF TIRE FAILURE CODE:
                                           BST =BLISTER
                                           BLW =BLOWOUT
                                           TTL =CRACK
                                           OFR =OUT OF ROUND
                                           TSW =PUNCTURE
                                           TTR =ROAD HAZARD
                                           TSP =TREAD SEPARATION
37      ORIG_EQUIP_YN     CHAR(1)       WAS PART ORIGINAL EQUIPMENT 'Y' OR 'N'
38      MANUF_DT          CHAR(8)       DATE OF MANUFACTURE (YYYYMMDD)
39      SEAT_TYPE         CHAR(4)       TYPE OF CHILD SEAT CODE:
                                           B  =BOOSTER
                                           C  =CONVERTIBLE
                                           I  =INFANT
                                           IN =INTEGRATED
                                           TD =TODDLER
40     RESTRAINT_TYPE     CHAR(4)       INSTALLATION SYSTEM CODE;
                                           A =VEHICLE SAFETY BELT
                                           B =LATCH SYSTEM
41     DEALER_NAME        CHAR(40)      DEALER'S NAME
42     DEALER_TEL         CHAR(20)      DEALER'S TELEPHONE NUMBER
43     DEALER_CITY        CHAR(30)      DEALER'S CITY
44     DEALER_STATE       CHAR(2)       DEALER'S STATE CODE
45     DEALER_ZIP         CHAR(10)      DEALER'S ZIPCODE
46     PROD_TYPE          CHAR(4)       PRODUCT TYPE CODE:
                                           V =VEHICLE
                                           T =TIRES
                                           E =EQUIPMENT
                                           C =CHILD RESTRAINT
47     REPAIRED_YN        CHAR(1)       WAS DEFECTIVE TIRE REPAIRED 'Y' OR 'N'
48     MEDICAL_ATTN       CHAR(1)       WAS MEDICAL ATTENTION REQUIRED 'Y' OR 'N'
49     VEHICLES_TOWED_YN  CHAR(1)       WAS VEHICLE TOWED 'Y' OR 'N'

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.
