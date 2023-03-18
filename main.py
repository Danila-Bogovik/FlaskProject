from flask import Flask, request, jsonify
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from postgres import psycopg2
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


app = Flask(__name__)

app.config['SECRET_KEY'] = "somekey"
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1@localhost:5432/users'

api = Api()

db = SQLAlchemy(app)

class data_set(db.Model):
	UES_ARM = db.Column(db.String(255))
	LTTS = db.Column(db.String(255))
	Nomer_zayavki = db.Column(db.String(255) , primary_key = True)
	Nomer_paketnoy_zayavki_MPZ = db.Column(db.String(255))
	Vneshniy_istochnik_zayavki = db.Column(db.String(255))
	Nmr_zayavk_iz_vnesh_istochnika = db.Column(db.String(255))
	Klient = db.Column(db.String(255))
	INN = db.Column(db.String(255))
	NLS = db.Column(db.String(255))
	Region = db.Column(db.String(255))
	Indeks = db.Column(db.String(255))
	Administrativnyiy_rayon = db.Column(db.String(255))
	Naselennyiy_punkt = db.Column(db.String(255))
	Ulitsa = db.Column(db.String(255))
	Dom = db.Column(db.String(255))
	Korpus = db.Column(db.String(255))
	Kvartira = db.Column(db.String(255))
	Adres_ustroystva = db.Column(db.String(255))
	Status = db.Column(db.String(255))
	Data_vhoda_zayavki_v_status = db.Column(db.String(255))
	Zadacha_po_zayavke = db.Column(db.String(255))
	Usluga = db.Column(db.String(255))
	Kolichestvo_uslug = db.Column(db.String(255))
	Dop_kanal_prodazh = db.Column(db.String(255))
	Tabelnyiy_nomer = db.Column(db.String(255))
	Naznachenie = db.Column(db.String(255))
	Kanal_prodazh = db.Column(db.String(255))
	Segment = db.Column(db.String(255))
	GTSSTS = db.Column(db.String(255))
	Data_obrascheniya = db.Column(db.String(255))
	Data_registratsii_zayavki = db.Column(db.String(255))
	Data_registratsii_pod_zayavki = db.Column(db.String(255))
	Reg_naryada_na_TVP = db.Column(db.String(255))
	Zavershena_vruchnuyu = db.Column(db.String(255))
	Prichina_otkaza_klienta = db.Column(db.String(255))
	Operator_zavershivshiy_zayavku = db.Column(db.String(255))
	Data_otkloneniya_pod_zayavki = db.Column(db.String(255))
	Otklonena = db.Column(db.String(255))
	Tip_proverki_TVP = db.Column(db.String(255))
	Nalichie_TVP = db.Column(db.String(255))
	Zavershenie_proverki_TVP = db.Column(db.String(255))
	Dlit_proverki_TVP = db.Column(db.String(255))
	Norm_srok_proverki_TVP_chas = db.Column(db.String(255))
	prevyish_norm_sroka_proverki_TVP = db.Column(db.String(255))
	Tehnologiya = db.Column(db.String(255))
	Sozdanie_dogovora = db.Column(db.String(255))
	Data_registr_naryada_na_naznach_TD = db.Column(db.String(255))
	Naznachenie_TD = db.Column(db.String(255))
	Tip_Naznacheniya_TD = db.Column(db.String(255))
	Dlit_naznacheniya_TD = db.Column(db.String(255))
	Norm_srok_naznacheniya_TD_chas = db.Column(db.String(255))
	prevyish_norm_sroka_naznacheniya_TD = db.Column(db.String(255))
	Data_cogl_vrem_vyiezd_instal_perv = db.Column(db.String(255))
	Soglapodklta_podkl_pervaya = db.Column(db.String(255))
	Soglasovannaya_data_podkl = db.Column(db.String(255))
	Zakryitie_naryada_na_podkl = db.Column(db.String(255))
	Norm_srok_podkl_dni = db.Column(db.String(255))
	Prevyishenie_norm_sroka_podkl = db.Column(db.String(255))
	Prevyipodkl_sroka_podkl__dni = db.Column(db.String(255))
	Data_vyipolneniya_agentom = db.Column(db.String(255))
	Data_peredachi_agentu = db.Column(db.String(255))
	Instalyator = db.Column(db.String(255))
	Agent_installyator = db.Column(db.String(255))
	Dlitpodklya_ot_reg_zayavki_v_IS = db.Column(db.String(255))
	Dlitpodklya_ot_reg_zayavki_v_IS_dni = db.Column(db.String(255))
	Kol_vo_perenosov_srokov = db.Column(db.String(255))
	Opisanie_prichinyi_perenosa_srokov = db.Column(db.String(255))
	Prichina_perenosa_srokov = db.Column(db.String(255))
	Annulirovan_pri_nalichii_TVP = db.Column(db.String(255))
	Vyisvobozhdenie_nazn_TD = db.Column(db.String(255))
	Dlitelnost_rezervir_TD = db.Column(db.String(255))
	Data_nachala_deystv_dogovora_KURS = db.Column(db.String(255))
	Sertifikat_OTA = db.Column(db.String(255))
	Sertifikat_OTA_aktivirovan = db.Column(db.String(255))
	Sertifikat_OTA_otklonen = db.Column(db.String(255))
	Sertifikat_Internet = db.Column(db.String(255))
	Sertifikat_Internet_aktivirovan = db.Column(db.String(255))
	Sertifikat_Internet_otklonen = db.Column(db.String(255))
	Sertifikat_IPTV = db.Column(db.String(255))
	Sertifikat_IPTV_aktivirovan = db.Column(db.String(255))
	Sertifikat_IPTV_otklonen = db.Column(db.String(255))
	Kommentariy_TVP_OTA = db.Column(db.String(255))
	Kommentariy_TVP_SHPD = db.Column(db.String(255))
	Operator_zavodivshiy_zayavku = db.Column(db.String(255))
	Kategoriya_uslugi_PK = db.Column(db.String(255))
	Internet = db.Column(db.String(255))
	IP_TV = db.Column(db.String(255))
	OTA = db.Column(db.String(255))
	Pryamoy_provod = db.Column(db.String(255))
	Fly = db.Column(db.String(255))
	MVNO = db.Column(db.String(255))
	Kolichestvo_SIM_kart = db.Column(db.String(255))
	Nachalo_zadachi_Dop_TO = db.Column(db.String(255))
	Okonchanie_zadachi_Dop_TO = db.Column(db.String(255))
	LS_Onima = db.Column(db.String(255))
	Prichinyi_otsutstviya_TVP = db.Column(db.String(255))
	Prichinyi_otsutstviya_TVP_IPTV = db.Column(db.String(255))
	ID_Dogovor_KURS = db.Column(db.String(255))
	Nomer_dogovora_KURS = db.Column(db.String(255))
	Dlitelnost_Dop_TO_dney = db.Column(db.String(255))
	Normsrok_Dop_TO_dney = db.Column(db.String(255))
	Naryad_KURS = db.Column(db.String(255))
	Data_zakryitiya_naryada_KURS = db.Column(db.String(255))
	Naryad_IPTV_KURS = db.Column(db.String(255))
	Data_otkryitiya_naryada_KURS = db.Column(db.String(255))
	Data_zakryitiya_naryada_IPTV_KURS = db.Column(db.String(255))
	Nomer_OTA_SHPD = db.Column(db.String(255))
	Data_otkryitiya_naryada_IPTV_KURS = db.Column(db.String(255))
	Primechanie = db.Column(db.String(255))
	Kontaktnyiy_telefon = db.Column(db.String(255))
	Kontaktnoe_litso = db.Column(db.String(255))
	Fiz_litso = db.Column(db.String(255))
	YUr_litso = db.Column(db.String(255))
	Zakryitie_naryada_installyatorom = db.Column(db.String(255))
	N_zadachi_vrnet_TVP = db.Column(db.String(255))
	VIP_klient = db.Column(db.String(255))
	Stoimost_TP_SHPD = db.Column(db.String(255))
	Stoimost_TP_IPTV = db.Column(db.String(255))
	FIO_sotrudnika_sozdavshego_dogovor = db.Column(db.String(255))
	Tarifnyiy_plan_IPTV = db.Column(db.String(255))
	Nomer_kartyi_dostupa = db.Column(db.String(255))
	Nomer_kartyi_dostupa_IPTV = db.Column(db.String(255))
	Tarifnyiy_plan = db.Column(db.String(255))
	Data_privyazki_kartyi_v_Onyma_SHPD = db.Column(db.String(255))
	Data_privyazki_kartyi_v_Onyma_IPTV = db.Column(db.String(255))
	Data_aktivatsii_uslugi_v_Onyma_SHPD = db.Column(db.String(255))
	Data_aktivatsii_uslugi_v_Onyma_IPTV = db.Column(db.String(255))
	Srok_zaversheniya_ustanovki_WFM = db.Column(db.String(255))
	Uchastok_WFM = db.Column(db.String(255))
	Sozdano_sotrudnikom_RRS = db.Column(db.String(255))
	TSPO = db.Column(db.String(255))
	Uslugi = db.Column(db.String(255))
	Promo_aktsii = db.Column(db.String(255))
	Tip_klienta_dlya_OSV = db.Column(db.String(255))
	Kanal_postupleniya_zayavki = db.Column(db.String(255))
	Nomer_zakaza_CMS = db.Column(db.String(255))
	Primechanie_pri_otkl = db.Column(db.String(255))
	Germes_APTV = db.Column(db.String(255))
	Zayavka_ARM_20 = db.Column(db.String(255))
	N_klientskiy_SUS = db.Column(db.String(255))
	N_stroitelnyiy_SUS = db.Column(db.String(255))
	Etap_SUS = db.Column(db.String(255))
	Migratsiya_YUL = db.Column(db.String(255))
	Proekt_SUS_Germes = db.Column(db.String(255))
	Ferrari = db.Column(db.String(255))
	Ferrari_BZ = db.Column(db.String(255))
	Data_otpravki_na_APTV = db.Column(db.String(255))
	Data_okonchaniya_APTV_planiruemaya = db.Column(db.String(255))
	Data_okonchaniya_APTV_fakticheskaya = db.Column(db.String(255))
	Dlitelnost_etapa_APTV = db.Column(db.String(255))
	Data_otpravki_na_DO = db.Column(db.String(255))
	Data_okonchaniya_DO_planiruemaya = db.Column(db.String(255))
	Data_okonchaniya_DO_fakticheskaya = db.Column(db.String(255))
	Dlitelnost_etapa_DO = db.Column(db.String(255))
	Bronirovanie_cherez_Germes = db.Column(db.String(255))
	Bronirovanie_cherez_Argus_ruchnoe = db.Column(db.String(255))
	Svetofor_Germes_APTV = db.Column(db.String(255))
	GID_doma_ORPON = db.Column(db.String(255))
	Paketnoe_reshenie = db.Column(db.String(255))
	Marker_paketa = db.Column(db.String(255))
	Dopusluga_1 = db.Column(db.String(255))
	Dopusluga_2 = db.Column(db.String(255))
	Dopusluga_3 = db.Column(db.String(255))
	Zayavka_cherez_EPK = db.Column(db.String(255))
	Novyiy_klient = db.Column(db.String(255))




@app.route('/upload', methods=['POST'])
def upload_data():
	data = request.get_json()

	new_data = data_set(

 UES_ARM = data['UES_ARM'],
 LTTS = data['LTTS'],
 Nomer_zayavki = data['Nomer_zayavki'],
 Nomer_paketnoy_zayavki_MPZ = data['Nomer_paketnoy_zayavki_MPZ'],
 Vneshniy_istochnik_zayavki = data['Vneshniy_istochnik_zayavki'],
 Nmr_zayavk_iz_vnesh_istochnika = data['Nmr_zayavk_iz_vnesh_istochnika'],
 Klient = data['Klient'],
 INN = data['INN'],
 NLS = data['NLS'],
 Region = data['Region'],
 Indeks = data['Indeks'],
 Administrativnyiy_rayon = data['Administrativnyiy_rayon'],
 Naselennyiy_punkt = data['Naselennyiy_punkt'],
 Ulitsa = data['Ulitsa'],
 Dom = data['Dom'],
 Korpus = data['Korpus'],
 Kvartira = data['Kvartira'],
 Adres_ustroystva = data['Adres_ustroystva'],
 Status = data['Status'],
 Data_vhoda_zayavki_v_status = data['Data_vhoda_zayavki_v_status'],
 Zadacha_po_zayavke = data['Zadacha_po_zayavke'],
 Usluga = data['Usluga'],
 Kolichestvo_uslug = data['Kolichestvo_uslug'],
 Dop_kanal_prodazh = data['Dop_kanal_prodazh'],
 Tabelnyiy_nomer = data['Tabelnyiy_nomer'],
 Naznachenie = data['Naznachenie'],
 Kanal_prodazh = data['Kanal_prodazh'],
 Segment = data['Segment'],
 GTSSTS = data['GTSSTS'],
 Data_obrascheniya = data['Data_obrascheniya'],
 Data_registratsii_zayavki = data['Data_registratsii_zayavki'],
 Data_registratsii_pod_zayavki = data['Data_registratsii_pod_zayavki'],
 Reg_naryada_na_TVP = data['Reg_naryada_na_TVP'],
 Zavershena_vruchnuyu = data['Zavershena_vruchnuyu'],
 Prichina_otkaza_klienta = data['Prichina_otkaza_klienta'],
 Operator_zavershivshiy_zayavku = data['Operator_zavershivshiy_zayavku'],
 Data_otkloneniya_pod_zayavki = data['Data_otkloneniya_pod_zayavki'],
 Otklonena = data['Otklonena'],
 Tip_proverki_TVP = data['Tip_proverki_TVP'],
 Nalichie_TVP = data['Nalichie_TVP'],
 Zavershenie_proverki_TVP = data['Zavershenie_proverki_TVP'],
 Dlit_proverki_TVP = data['Dlit_proverki_TVP'],
 Norm_srok_proverki_TVP_chas = data['Norm_srok_proverki_TVP_chas'],
 prevyish_norm_sroka_proverki_TVP = data['prevyish_norm_sroka_proverki_TVP'],
 Tehnologiya = data['Tehnologiya'],
 Sozdanie_dogovora = data['Sozdanie_dogovora'],
 Data_registr_naryada_na_naznach_TD = data['Data_registr_naryada_na_naznach_TD'],
 Naznachenie_TD = data['Naznachenie_TD'],
 Tip_Naznacheniya_TD = data['Tip_Naznacheniya_TD'],
 Dlit_naznacheniya_TD = data['Dlit_naznacheniya_TD'],
 Norm_srok_naznacheniya_TD_chas = data['Norm_srok_naznacheniya_TD_chas'],
 prevyish_norm_sroka_naznacheniya_TD = data['prevyish_norm_sroka_naznacheniya_TD'],
 Data_cogl_vrem_vyiezd_instal_perv = data['Data_cogl_vrem_vyiezd_instal_perv'],
 Soglapodklta_podkl_pervaya = data['Soglapodklta_podkl_pervaya'],
 Soglasovannaya_data_podkl = data['Soglasovannaya_data_podkl'],
 Zakryitie_naryada_na_podkl = data['Zakryitie_naryada_na_podkl'],
 Norm_srok_podkl_dni = data['Norm_srok_podkl_dni'],
 Prevyishenie_norm_sroka_podkl = data['Prevyishenie_norm_sroka_podkl'],
 Prevyipodkl_sroka_podkl__dni = data['Prevyipodkl_sroka_podkl__dni'],
 Data_vyipolneniya_agentom = data['Data_vyipolneniya_agentom'],
 Data_peredachi_agentu = data['Data_peredachi_agentu'],
 Instalyator = data['Instalyator'],
 Agent_installyator = data['Agent_installyator'],
 Dlitpodklya_ot_reg_zayavki_v_IS = data['Dlitpodklya_ot_reg_zayavki_v_IS'],
 Dlitpodklya_ot_reg_zayavki_v_IS_dni = data['Dlitpodklya_ot_reg_zayavki_v_IS_dni'],
 Kol_vo_perenosov_srokov = data['Kol_vo_perenosov_srokov'],
 Opisanie_prichinyi_perenosa_srokov = data['Opisanie_prichinyi_perenosa_srokov'],
 Prichina_perenosa_srokov = data['Prichina_perenosa_srokov'],
 Annulirovan_pri_nalichii_TVP = data['Annulirovan_pri_nalichii_TVP'],
 Vyisvobozhdenie_nazn_TD = data['Vyisvobozhdenie_nazn_TD'],
 Dlitelnost_rezervir_TD = data['Dlitelnost_rezervir_TD'],
 Data_nachala_deystv_dogovora_KURS = data['Data_nachala_deystv_dogovora_KURS'],
 Sertifikat_OTA = data['Sertifikat_OTA'],
 Sertifikat_OTA_aktivirovan = data['Sertifikat_OTA_aktivirovan'],
 Sertifikat_OTA_otklonen = data['Sertifikat_OTA_otklonen'],
 Sertifikat_Internet = data['Sertifikat_Internet'],
 Sertifikat_Internet_aktivirovan = data['Sertifikat_Internet_aktivirovan'],
 Sertifikat_Internet_otklonen = data['Sertifikat_Internet_otklonen'],
 Sertifikat_IPTV = data['Sertifikat_IPTV'],
 Sertifikat_IPTV_aktivirovan = data['Sertifikat_IPTV_aktivirovan'],
 Sertifikat_IPTV_otklonen = data['Sertifikat_IPTV_otklonen'],
 Kommentariy_TVP_OTA = data['Kommentariy_TVP_OTA'],
 Kommentariy_TVP_SHPD = data['Kommentariy_TVP_SHPD'],
 Operator_zavodivshiy_zayavku = data['Operator_zavodivshiy_zayavku'],
 Kategoriya_uslugi_PK = data['Kategoriya_uslugi_PK'],
 Internet = data['Internet'],
 IP_TV = data['IP_TV'],
 OTA = data['OTA'],
 Pryamoy_provod = data['Pryamoy_provod'],
 Fly = data['Fly'],
 MVNO = data['MVNO'],
 Kolichestvo_SIM_kart = data['Kolichestvo_SIM_kart'],
 Nachalo_zadachi_Dop_TO = data['Nachalo_zadachi_Dop_TO'],
 Okonchanie_zadachi_Dop_TO = data['Okonchanie_zadachi_Dop_TO'],
 LS_Onima = data['LS_Onima'],
 Prichinyi_otsutstviya_TVP = data['Prichinyi_otsutstviya_TVP'],
 Prichinyi_otsutstviya_TVP_IPTV = data['Prichinyi_otsutstviya_TVP_IPTV'],
 ID_Dogovor_KURS = data['ID_Dogovor_KURS'],
 Nomer_dogovora_KURS = data['Nomer_dogovora_KURS'],
 Dlitelnost_Dop_TO_dney = data['Dlitelnost_Dop_TO_dney'],
 Normsrok_Dop_TO_dney = data['Normsrok_Dop_TO_dney'],
 Naryad_KURS = data['Naryad_KURS'],
 Data_zakryitiya_naryada_KURS = data['Data_zakryitiya_naryada_KURS'],
 Naryad_IPTV_KURS = data['Naryad_IPTV_KURS'],
 Data_otkryitiya_naryada_KURS = data['Data_otkryitiya_naryada_KURS'],
 Data_zakryitiya_naryada_IPTV_KURS = data['Data_zakryitiya_naryada_IPTV_KURS'],
 Nomer_OTA_SHPD = data['Nomer_OTA_SHPD'],
 Data_otkryitiya_naryada_IPTV_KURS = data['Data_otkryitiya_naryada_IPTV_KURS'],
 Primechanie = data['Primechanie'],
 Kontaktnyiy_telefon = data['Kontaktnyiy_telefon'],
 Kontaktnoe_litso = data['Kontaktnoe_litso'],
 Fiz_litso = data['Fiz_litso'],
 YUr_litso = data['YUr_litso'],
 Zakryitie_naryada_installyatorom = data['Zakryitie_naryada_installyatorom'],
 N_zadachi_vrnet_TVP = data['N_zadachi_vrnet_TVP'],
 VIP_klient = data['VIP_klient'],
 Stoimost_TP_SHPD = data['Stoimost_TP_SHPD'],
 Stoimost_TP_IPTV = data['Stoimost_TP_IPTV'],
 FIO_sotrudnika_sozdavshego_dogovor = data['FIO_sotrudnika_sozdavshego_dogovor'],
 Tarifnyiy_plan_IPTV = data['Tarifnyiy_plan_IPTV'],
 Nomer_kartyi_dostupa = data['Nomer_kartyi_dostupa'],
 Nomer_kartyi_dostupa_IPTV = data['Nomer_kartyi_dostupa_IPTV'],
 Tarifnyiy_plan = data['Tarifnyiy_plan'],
 Data_privyazki_kartyi_v_Onyma_SHPD = data['Data_privyazki_kartyi_v_Onyma_SHPD'],
 Data_privyazki_kartyi_v_Onyma_IPTV = data['Data_privyazki_kartyi_v_Onyma_IPTV'],
 Data_aktivatsii_uslugi_v_Onyma_SHPD = data['Data_aktivatsii_uslugi_v_Onyma_SHPD'],
 Data_aktivatsii_uslugi_v_Onyma_IPTV = data['Data_aktivatsii_uslugi_v_Onyma_IPTV'],
 Srok_zaversheniya_ustanovki_WFM = data['Srok_zaversheniya_ustanovki_WFM'],
 Uchastok_WFM = data['Uchastok_WFM'],
 Sozdano_sotrudnikom_RRS = data['Sozdano_sotrudnikom_RRS'],
 TSPO = data['TSPO'],
 Uslugi = data['Uslugi'],
 Promo_aktsii = data['Promo_aktsii'],
 Tip_klienta_dlya_OSV = data['Tip_klienta_dlya_OSV'],
 Kanal_postupleniya_zayavki = data['Kanal_postupleniya_zayavki'],
 Nomer_zakaza_CMS = data['Nomer_zakaza_CMS'],
 Primechanie_pri_otkl = data['Primechanie_pri_otkl'],
 Germes_APTV = data['Germes_APTV'],
 Zayavka_ARM_20 = data['Zayavka_ARM_20'],
 N_klientskiy_SUS = data['N_klientskiy_SUS'],
 N_stroitelnyiy_SUS = data['N_stroitelnyiy_SUS'],
 Etap_SUS = data['Etap_SUS'],
 Migratsiya_YUL = data['Migratsiya_YUL'],
 Proekt_SUS_Germes = data['Proekt_SUS_Germes'],
 Ferrari = data['Ferrari'],
 Ferrari_BZ = data['Ferrari_BZ'],
 Data_otpravki_na_APTV = data['Data_otpravki_na_APTV'],
 Data_okonchaniya_APTV_planiruemaya = data['Data_okonchaniya_APTV_planiruemaya'],
 Data_okonchaniya_APTV_fakticheskaya = data['Data_okonchaniya_APTV_fakticheskaya'],
 Dlitelnost_etapa_APTV = data['Dlitelnost_etapa_APTV'],
 Data_otpravki_na_DO = data['Data_otpravki_na_DO'],
 Data_okonchaniya_DO_planiruemaya = data['Data_okonchaniya_DO_planiruemaya'],
 Data_okonchaniya_DO_fakticheskaya = data['Data_okonchaniya_DO_fakticheskaya'],
 Dlitelnost_etapa_DO = data['Dlitelnost_etapa_DO'],
 Bronirovanie_cherez_Germes = data['Bronirovanie_cherez_Germes'],
 Bronirovanie_cherez_Argus_ruchnoe = data['Bronirovanie_cherez_Argus_ruchnoe'],
 Svetofor_Germes_APTV = data['Svetofor_Germes_APTV'],
 GID_doma_ORPON = data['GID_doma_ORPON'],
 Paketnoe_reshenie = data['Paketnoe_reshenie'],
 Marker_paketa = data['Marker_paketa'],
 Dopusluga_1 = data['Dopusluga_1'],
 Dopusluga_2 = data['Dopusluga_2'],
 Dopusluga_3 = data['Dopusluga_3'],
 Zayavka_cherez_EPK = data['Zayavka_cherez_EPK'],
 Novyiy_klient = data['Novyiy_klient'] )

	db.session.add(new_data)
	db.session.commit()

	return "++"


# @app.route('/request', methods=['GET'])
# def send_data():

# data = data_set.query.all()

# 	user_data = {}

# 	for user in data:
# 		user_data['id'] = user.id
# 		user_data['role'] = user.role
# 		user_data['name'] = user.name
# 		user_data['surename'] = user.surename
# 		user_data['password'] = user.password

# 	return jsonify(user_data)





api.init_app(app)






if __name__ == "__main__":
	app.run(debug=True, port=3000, host="127.0.0.1")





# ВНИЗУ МАТЕРИАЛ ДЛЯ РАБОТЫ, НЕ КОД










class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	role = db.Column(db.Integer)
	name = db.Column(db.String(50))
	surename = db.Column(db.String(50))
	password = db.Column(db.String(80))
	icon_link = db.Column(db.String(255))

api = Api()

#вход в личный кабинет
@app.route('/profile', methods=['GET'])
def get_user_info():

	users = User.query.all()

	user_data = {}

	for user in users:
		user_data['id'] = user.id
		user_data['role'] = user.role
		user_data['name'] = user.name
		user_data['surename'] = user.surename
		user_data['password'] = user.password

	return jsonify(user_data)

#регистрация
@app.route('/register', methods=['POST'])
def create_user():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method = 'sha256')
	
	new_user = User(id=data['id'], name = data['name'], surename = data['surename'], 
		password = hashed_password, role = data['role'])

	db.session.add(new_user)
	db.session.commit()

	access_token = create_access_token(identity = data['username'])
	refresh_token = create_refresh_token(identity = data['username'])
	return "++"


# вход в систему
@app.route('/login', methods=['POST'])
def user_login():
	return ""

































