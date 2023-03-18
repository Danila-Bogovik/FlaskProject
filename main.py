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
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1@localhost:5432/USERS'



jwt = JWTManager(app)
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
 №_zadachi_vrnet_TVP = db.Column(db.String(255))
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
 №_klientskiy_SUS = db.Column(db.String(255))
 №_stroitelnyiy_SUS = db.Column(db.String(255))
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


@app.route('/upload', methods=['POST'])
def upload_data():
	data = request.get_json()

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



api.init_app(app)


if __name__ == "__main__":
	app.run(debug=True, port=3000, host="127.0.0.1")