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
	ues_arm = db.Column(db.String(255)) 
	ltts = db.Column(db.String(255)) 
 nomer_zayavki = db.Column(db.String(255)) 
 nomer_paketnoy_zayavki_mpz = db.Column(db.String(255)) 
 vneshniy_istochnik_zayavki = db.Column(db.String(255)) 
 nmr_zayavk_iz_vnesh_istochnika = db.Column(db.String(255)) 
 klient = db.Column(db.String(255)) 
 inn = db.Column(db.String(255)) 
 nls = db.Column(db.String(255)) 
 region = db.Column(db.String(255)) 
 indeks = db.Column(db.String(255)) 
 administrativnyiy_rayon = db.Column(db.String(255)) 
 naselennyiy_punkt = db.Column(db.String(255)) 
 ulitsa = db.Column(db.String(255)) 
 dom = db.Column(db.String(255)) 
 korpus = db.Column(db.String(255)) 
 kvartira = db.Column(db.String(255)) 
 adres_ustroystva = db.Column(db.String(255)) 
 status = db.Column(db.String(255)) 
 data_vhoda_zayavki_v_status = db.Column(db.String(255)) 
 zadacha_po_zayavke = db.Column(db.String(255)) 
 usluga = db.Column(db.String(255)) 
 kolichestvo_uslug = db.Column(db.String(255)) 
 dop_kanal_prodazh = db.Column(db.String(255)) 
 tabelnyiy_nomer = db.Column(db.String(255)) 
 naznachenie = db.Column(db.String(255)) 
 kanal_prodazh = db.Column(db.String(255)) 
 segment = db.Column(db.String(255)) 
 gtssts = db.Column(db.String(255)) 
 data_obrascheniya = db.Column(db.String(255)) 
 data_registratsii_zayavki = db.Column(db.String(255)) 
 data_registratsii_pod_zayavki = db.Column(db.String(255)) 
 reg_naryada_na_tvp = db.Column(db.String(255)) 
 zavershena_vruchnuyu = db.Column(db.String(255)) 
 prichina_otkaza_klienta = db.Column(db.String(255)) 
 operator_zavershivshiy_zayavku = db.Column(db.String(255)) 
 data_otkloneniya_pod_zayavki = db.Column(db.String(255)) 
 otklonena = db.Column(db.String(255)) 
 tip_proverki_tvp = db.Column(db.String(255)) 
 nalichie_tvp = db.Column(db.String(255)) 
 zavershenie_proverki_tvp = db.Column(db.String(255)) 
 dlit_proverki_tvp = db.Column(db.String(255)) 
 norm_srok_proverki_tvp_chas = db.Column(db.String(255)) 
 prevyish_norm_sroka_proverki_tvp = db.Column(db.String(255)) 
 tehnologiya = db.Column(db.String(255)) 
 sozdanie_dogovora = db.Column(db.String(255)) 
 data_registr_naryada_na_naznach_td = db.Column(db.String(255)) 
 naznachenie_td = db.Column(db.String(255)) 
 tip_naznacheniya_td = db.Column(db.String(255)) 
 dlit_naznacheniya_td = db.Column(db.String(255)) 
 norm_srok_naznacheniya_td_chas = db.Column(db.String(255)) 
 prevyish_norm_sroka_naznacheniya_td = db.Column(db.String(255)) 
 data_cogl_vrem_vyiezd_instal_perv = db.Column(db.String(255)) 
 soglapodklta_podkl_pervaya = db.Column(db.String(255)) 
 soglasovannaya_data_podkl = db.Column(db.String(255)) 
 zakryitie_naryada_na_podkl = db.Column(db.String(255)) 
 norm_srok_podkl_dni = db.Column(db.String(255)) 
 prevyishenie_norm_sroka_podkl = db.Column(db.String(255)) 
 prevyipodkl_sroka_podkl__dni = db.Column(db.String(255)) 
 data_vyipolneniya_agentom = db.Column(db.String(255)) 
 data_peredachi_agentu = db.Column(db.String(255)) 
 instalyator = db.Column(db.String(255)) 
 agent_installyator = db.Column(db.String(255)) 
 dlitpodklya_ot_reg_zayavki_v_is = db.Column(db.String(255)) 
 dlitpodklya_ot_reg_zayavki_v_is_dni = db.Column(db.String(255)) 
 kol_vo_perenosov_srokov = db.Column(db.String(255)) 
 opisanie_prichinyi_perenosa_srokov = db.Column(db.String(255)) 
 prichina_perenosa_srokov = db.Column(db.String(255)) 
 annulirovan_pri_nalichii_tvp = db.Column(db.String(255)) 
 vyisvobozhdenie_nazn_td = db.Column(db.String(255)) 
 dlitelnost_rezervir_td = db.Column(db.String(255)) 
 data_nachala_deystv_dogovora_kurs = db.Column(db.String(255)) 
 sertifikat_ota = db.Column(db.String(255)) 
 sertifikat_ota_aktivirovan = db.Column(db.String(255)) 
 sertifikat_ota_otklonen = db.Column(db.String(255)) 
 sertifikat_internet = db.Column(db.String(255)) 
 sertifikat_internet_aktivirovan = db.Column(db.String(255)) 
 sertifikat_internet_otklonen = db.Column(db.String(255)) 
 sertifikat_iptv = db.Column(db.String(255)) 
 sertifikat_iptv_aktivirovan = db.Column(db.String(255)) 
 sertifikat_iptv_otklonen = db.Column(db.String(255)) 
 kommentariy_tvp_ota = db.Column(db.String(255)) 
 kommentariy_tvp_shpd = db.Column(db.String(255)) 
 operator_zavodivshiy_zayavku = db.Column(db.String(255)) 
 kategoriya_uslugi_pk = db.Column(db.String(255)) 
 internet = db.Column(db.String(255)) 
 ip_tv = db.Column(db.String(255)) 
 ota = db.Column(db.String(255)) 
 pryamoy_provod = db.Column(db.String(255)) 
 fly = db.Column(db.String(255)) 
 mvno = db.Column(db.String(255)) 
 kolichestvo_sim_kart = db.Column(db.String(255)) 
 nachalo_zadachi_dop_to = db.Column(db.String(255)) 
 okonchanie_zadachi_dop_to = db.Column(db.String(255)) 
 ls_onima = db.Column(db.String(255)) 
 prichinyi_otsutstviya_tvp = db.Column(db.String(255)) 
 prichinyi_otsutstviya_tvp_iptv = db.Column(db.String(255)) 
 id_dogovor_kurs = db.Column(db.String(255)) 
 nomer_dogovora_kurs = db.Column(db.String(255)) 
 dlitelnost_dop_to_dney = db.Column(db.String(255)) 
 normsrok_dop_to_dney = db.Column(db.String(255)) 
 naryad_kurs = db.Column(db.String(255)) 
 data_zakryitiya_naryada_kurs = db.Column(db.String(255)) 
 naryad_iptv_kurs = db.Column(db.String(255)) 
 data_otkryitiya_naryada_kurs = db.Column(db.String(255)) 
 data_zakryitiya_naryada_iptv_kurs = db.Column(db.String(255)) 
 nomer_ota_shpd = db.Column(db.String(255)) 
 data_otkryitiya_naryada_iptv_kurs = db.Column(db.String(255)) 
 primechanie = db.Column(db.String(255)) 
 kontaktnyiy_telefon = db.Column(db.String(255)) 
 kontaktnoe_litso = db.Column(db.String(255)) 
 fiz_litso = db.Column(db.String(255)) 
 yur_litso = db.Column(db.String(255)) 
 zakryitie_naryada_installyatorom = db.Column(db.String(255)) 
 n_zadachi_vrnet_tvp = db.Column(db.String(255)) 
 vip_klient = db.Column(db.String(255)) 
 stoimost_tp_shpd = db.Column(db.String(255)) 
 stoimost_tp_iptv = db.Column(db.String(255)) 
 fio_sotrudnika_sozdavshego_dogovor = db.Column(db.String(255)) 
 tarifnyiy_plan_iptv = db.Column(db.String(255)) 
 nomer_kartyi_dostupa = db.Column(db.String(255)) 
 nomer_kartyi_dostupa_iptv = db.Column(db.String(255)) 
 tarifnyiy_plan = db.Column(db.String(255)) 
 data_privyazki_kartyi_v_onyma_shpd = db.Column(db.String(255)) 
 data_privyazki_kartyi_v_onyma_iptv = db.Column(db.String(255)) 
 data_aktivatsii_uslugi_v_onyma_shpd = db.Column(db.String(255)) 
 data_aktivatsii_uslugi_v_onyma_iptv = db.Column(db.String(255)) 
 srok_zaversheniya_ustanovki_wfm = db.Column(db.String(255)) 
 uchastok_wfm = db.Column(db.String(255)) 
 sozdano_sotrudnikom_rrs = db.Column(db.String(255)) 
 tspo = db.Column(db.String(255)) 
 uslugi = db.Column(db.String(255)) 
 promo_aktsii = db.Column(db.String(255)) 
 tip_klienta_dlya_osv = db.Column(db.String(255)) 
 kanal_postupleniya_zayavki = db.Column(db.String(255)) 
 nomer_zakaza_cms = db.Column(db.String(255)) 
 primechanie_pri_otkl = db.Column(db.String(255)) 
 germes_aptv = db.Column(db.String(255)) 
 zayavka_arm_20 = db.Column(db.String(255)) 
 n_klientskiy_sus = db.Column(db.String(255)) 
 n_stroitelnyiy_sus = db.Column(db.String(255)) 
 etap_sus = db.Column(db.String(255)) 
 migratsiya_yul = db.Column(db.String(255)) 
 proekt_sus_germes = db.Column(db.String(255)) 
 ferrari = db.Column(db.String(255)) 
 ferrari_bz = db.Column(db.String(255)) 
 data_otpravki_na_aptv = db.Column(db.String(255)) 
 data_okonchaniya_aptv_planiruemaya = db.Column(db.String(255)) 
 data_okonchaniya_aptv_fakticheskaya = db.Column(db.String(255)) 
 dlitelnost_etapa_aptv = db.Column(db.String(255)) 
 data_otpravki_na_do = db.Column(db.String(255)) 
 data_okonchaniya_do_planiruemaya = db.Column(db.String(255)) 
 data_okonchaniya_do_fakticheskaya = db.Column(db.String(255)) 
 dlitelnost_etapa_do = db.Column(db.String(255)) 
 bronirovanie_cherez_germes = db.Column(db.String(255)) 
 bronirovanie_cherez_argus_ruchnoe = db.Column(db.String(255)) 
 svetofor_germes_aptv = db.Column(db.String(255)) 
 gid_doma_orpon = db.Column(db.String(255)) 
 paketnoe_reshenie = db.Column(db.String(255)) 
 marker_paketa = db.Column(db.String(255)) 
 dopusluga_1 = db.Column(db.String(255)) 
 dopusluga_2 = db.Column(db.String(255)) 
 dopusluga_3 = db.Column(db.String(255)) 
 zayavka_cherez_epk = db.Column(db.String(255)) 
 novyiy_klient = db.Column(db.String(255)) 




@app.route('/upload', methods=['POST'])
def upload_data():
	data = request.get_json()

	new_data = data_set(
		ues_arm = data['ues_arm'], 
 ltts = data['ltts'], 
 nomer_zayavki = data['nomer_zayavki'], 
 nomer_paketnoy_zayavki_mpz = data['nomer_paketnoy_zayavki_mpz'], 
 vneshniy_istochnik_zayavki = data['vneshniy_istochnik_zayavki'], 
 nmr_zayavk_iz_vnesh_istochnika = data['nmr_zayavk_iz_vnesh_istochnika'], 
 klient = data['klient'], 
 inn = data['inn'], 
 nls = data['nls'], 
 region = data['region'], 
 indeks = data['indeks'], 
 administrativnyiy_rayon = data['administrativnyiy_rayon'], 
 naselennyiy_punkt = data['naselennyiy_punkt'], 
 ulitsa = data['ulitsa'], 
 dom = data['dom'], 
 korpus = data['korpus'], 
 kvartira = data['kvartira'], 
 adres_ustroystva = data['adres_ustroystva'], 
 status = data['status'], 
 data_vhoda_zayavki_v_status = data['data_vhoda_zayavki_v_status'], 
 zadacha_po_zayavke = data['zadacha_po_zayavke'], 
 usluga = data['usluga'], 
 kolichestvo_uslug = data['kolichestvo_uslug'], 
 dop_kanal_prodazh = data['dop_kanal_prodazh'], 
 tabelnyiy_nomer = data['tabelnyiy_nomer'], 
 naznachenie = data['naznachenie'], 
 kanal_prodazh = data['kanal_prodazh'], 
 segment = data['segment'], 
 gtssts = data['gtssts'], 
 data_obrascheniya = data['data_obrascheniya'], 
 data_registratsii_zayavki = data['data_registratsii_zayavki'], 
 data_registratsii_pod_zayavki = data['data_registratsii_pod_zayavki'], 
 reg_naryada_na_tvp = data['reg_naryada_na_tvp'], 
 zavershena_vruchnuyu = data['zavershena_vruchnuyu'], 
 prichina_otkaza_klienta = data['prichina_otkaza_klienta'], 
 operator_zavershivshiy_zayavku = data['operator_zavershivshiy_zayavku'], 
 data_otkloneniya_pod_zayavki = data['data_otkloneniya_pod_zayavki'], 
 otklonena = data['otklonena'], 
 tip_proverki_tvp = data['tip_proverki_tvp'], 
 nalichie_tvp = data['nalichie_tvp'], 
 zavershenie_proverki_tvp = data['zavershenie_proverki_tvp'], 
 dlit_proverki_tvp = data['dlit_proverki_tvp'], 
 norm_srok_proverki_tvp_chas = data['norm_srok_proverki_tvp_chas'], 
 prevyish_norm_sroka_proverki_tvp = data['prevyish_norm_sroka_proverki_tvp'], 
 tehnologiya = data['tehnologiya'], 
 sozdanie_dogovora = data['sozdanie_dogovora'], 
 data_registr_naryada_na_naznach_td = data['data_registr_naryada_na_naznach_td'], 
 naznachenie_td = data['naznachenie_td'], 
 tip_naznacheniya_td = data['tip_naznacheniya_td'], 
 dlit_naznacheniya_td = data['dlit_naznacheniya_td'], 
 norm_srok_naznacheniya_td_chas = data['norm_srok_naznacheniya_td_chas'], 
 prevyish_norm_sroka_naznacheniya_td = data['prevyish_norm_sroka_naznacheniya_td'], 
 data_cogl_vrem_vyiezd_instal_perv = data['data_cogl_vrem_vyiezd_instal_perv'], 
 soglapodklta_podkl_pervaya = data['soglapodklta_podkl_pervaya'], 
 soglasovannaya_data_podkl = data['soglasovannaya_data_podkl'], 
 zakryitie_naryada_na_podkl = data['zakryitie_naryada_na_podkl'], 
 norm_srok_podkl_dni = data['norm_srok_podkl_dni'], 
 prevyishenie_norm_sroka_podkl = data['prevyishenie_norm_sroka_podkl'], 
 prevyipodkl_sroka_podkl__dni = data['prevyipodkl_sroka_podkl__dni'], 
 data_vyipolneniya_agentom = data['data_vyipolneniya_agentom'], 
 data_peredachi_agentu = data['data_peredachi_agentu'], 
 instalyator = data['instalyator'], 
 agent_installyator = data['agent_installyator'], 
 dlitpodklya_ot_reg_zayavki_v_is = data['dlitpodklya_ot_reg_zayavki_v_is'], 
 dlitpodklya_ot_reg_zayavki_v_is_dni = data['dlitpodklya_ot_reg_zayavki_v_is_dni'], 
 kol_vo_perenosov_srokov = data['kol_vo_perenosov_srokov'], 
 opisanie_prichinyi_perenosa_srokov = data['opisanie_prichinyi_perenosa_srokov'], 
 prichina_perenosa_srokov = data['prichina_perenosa_srokov'], 
 annulirovan_pri_nalichii_tvp = data['annulirovan_pri_nalichii_tvp'], 
 vyisvobozhdenie_nazn_td = data['vyisvobozhdenie_nazn_td'], 
 dlitelnost_rezervir_td = data['dlitelnost_rezervir_td'], 
 data_nachala_deystv_dogovora_kurs = data['data_nachala_deystv_dogovora_kurs'], 
 sertifikat_ota = data['sertifikat_ota'], 
 sertifikat_ota_aktivirovan = data['sertifikat_ota_aktivirovan'], 
 sertifikat_ota_otklonen = data['sertifikat_ota_otklonen'], 
 sertifikat_internet = data['sertifikat_internet'], 
 sertifikat_internet_aktivirovan = data['sertifikat_internet_aktivirovan'], 
 sertifikat_internet_otklonen = data['sertifikat_internet_otklonen'], 
 sertifikat_iptv = data['sertifikat_iptv'], 
 sertifikat_iptv_aktivirovan = data['sertifikat_iptv_aktivirovan'], 
 sertifikat_iptv_otklonen = data['sertifikat_iptv_otklonen'], 
 kommentariy_tvp_ota = data['kommentariy_tvp_ota'], 
 kommentariy_tvp_shpd = data['kommentariy_tvp_shpd'], 
 operator_zavodivshiy_zayavku = data['operator_zavodivshiy_zayavku'], 
 kategoriya_uslugi_pk = data['kategoriya_uslugi_pk'], 
 internet = data['internet'], 
 ip_tv = data['ip_tv'], 
 ota = data['ota'], 
 pryamoy_provod = data['pryamoy_provod'], 
 fly = data['fly'], 
 mvno = data['mvno'], 
 kolichestvo_sim_kart = data['kolichestvo_sim_kart'], 
 nachalo_zadachi_dop_to = data['nachalo_zadachi_dop_to'], 
 okonchanie_zadachi_dop_to = data['okonchanie_zadachi_dop_to'], 
 ls_onima = data['ls_onima'], 
 prichinyi_otsutstviya_tvp = data['prichinyi_otsutstviya_tvp'], 
 prichinyi_otsutstviya_tvp_iptv = data['prichinyi_otsutstviya_tvp_iptv'], 
 id_dogovor_kurs = data['id_dogovor_kurs'], 
 nomer_dogovora_kurs = data['nomer_dogovora_kurs'], 
 dlitelnost_dop_to_dney = data['dlitelnost_dop_to_dney'], 
 normsrok_dop_to_dney = data['normsrok_dop_to_dney'], 
 naryad_kurs = data['naryad_kurs'], 
 data_zakryitiya_naryada_kurs = data['data_zakryitiya_naryada_kurs'], 
 naryad_iptv_kurs = data['naryad_iptv_kurs'], 
 data_otkryitiya_naryada_kurs = data['data_otkryitiya_naryada_kurs'], 
 data_zakryitiya_naryada_iptv_kurs = data['data_zakryitiya_naryada_iptv_kurs'], 
 nomer_ota_shpd = data['nomer_ota_shpd'], 
 data_otkryitiya_naryada_iptv_kurs = data['data_otkryitiya_naryada_iptv_kurs'], 
 primechanie = data['primechanie'], 
 kontaktnyiy_telefon = data['kontaktnyiy_telefon'], 
 kontaktnoe_litso = data['kontaktnoe_litso'], 
 fiz_litso = data['fiz_litso'], 
 yur_litso = data['yur_litso'], 
 zakryitie_naryada_installyatorom = data['zakryitie_naryada_installyatorom'], 
 n_zadachi_vrnet_tvp = data['n_zadachi_vrnet_tvp'], 
 vip_klient = data['vip_klient'], 
 stoimost_tp_shpd = data['stoimost_tp_shpd'], 
 stoimost_tp_iptv = data['stoimost_tp_iptv'], 
 fio_sotrudnika_sozdavshego_dogovor = data['fio_sotrudnika_sozdavshego_dogovor'], 
 tarifnyiy_plan_iptv = data['tarifnyiy_plan_iptv'], 
 nomer_kartyi_dostupa = data['nomer_kartyi_dostupa'], 
 nomer_kartyi_dostupa_iptv = data['nomer_kartyi_dostupa_iptv'], 
 tarifnyiy_plan = data['tarifnyiy_plan'], 
 data_privyazki_kartyi_v_onyma_shpd = data['data_privyazki_kartyi_v_onyma_shpd'], 
 data_privyazki_kartyi_v_onyma_iptv = data['data_privyazki_kartyi_v_onyma_iptv'], 
 data_aktivatsii_uslugi_v_onyma_shpd = data['data_aktivatsii_uslugi_v_onyma_shpd'], 
 data_aktivatsii_uslugi_v_onyma_iptv = data['data_aktivatsii_uslugi_v_onyma_iptv'], 
 srok_zaversheniya_ustanovki_wfm = data['srok_zaversheniya_ustanovki_wfm'], 
 uchastok_wfm = data['uchastok_wfm'], 
 sozdano_sotrudnikom_rrs = data['sozdano_sotrudnikom_rrs'], 
 tspo = data['tspo'], 
 uslugi = data['uslugi'], 
 promo_aktsii = data['promo_aktsii'], 
 tip_klienta_dlya_osv = data['tip_klienta_dlya_osv'], 
 kanal_postupleniya_zayavki = data['kanal_postupleniya_zayavki'], 
 nomer_zakaza_cms = data['nomer_zakaza_cms'], 
 primechanie_pri_otkl = data['primechanie_pri_otkl'], 
 germes_aptv = data['germes_aptv'], 
 zayavka_arm_20 = data['zayavka_arm_20'], 
 n_klientskiy_sus = data['n_klientskiy_sus'], 
 n_stroitelnyiy_sus = data['n_stroitelnyiy_sus'], 
 etap_sus = data['etap_sus'], 
 migratsiya_yul = data['migratsiya_yul'], 
 proekt_sus_germes = data['proekt_sus_germes'], 
 ferrari = data['ferrari'], 
 ferrari_bz = data['ferrari_bz'], 
 data_otpravki_na_aptv = data['data_otpravki_na_aptv'], 
 data_okonchaniya_aptv_planiruemaya = data['data_okonchaniya_aptv_planiruemaya'], 
 data_okonchaniya_aptv_fakticheskaya = data['data_okonchaniya_aptv_fakticheskaya'], 
 dlitelnost_etapa_aptv = data['dlitelnost_etapa_aptv'], 
 data_otpravki_na_do = data['data_otpravki_na_do'], 
 data_okonchaniya_do_planiruemaya = data['data_okonchaniya_do_planiruemaya'], 
 data_okonchaniya_do_fakticheskaya = data['data_okonchaniya_do_fakticheskaya'], 
 dlitelnost_etapa_do = data['dlitelnost_etapa_do'], 
 bronirovanie_cherez_germes = data['bronirovanie_cherez_germes'], 
 bronirovanie_cherez_argus_ruchnoe = data['bronirovanie_cherez_argus_ruchnoe'], 
 svetofor_germes_aptv = data['svetofor_germes_aptv'], 
 gid_doma_orpon = data['gid_doma_orpon'], 
 paketnoe_reshenie = data['paketnoe_reshenie'], 
 marker_paketa = data['marker_paketa'], 
 dopusluga_1 = data['dopusluga_1'], 
 dopusluga_2 = data['dopusluga_2'], 
 dopusluga_3 = data['dopusluga_3'], 
 zayavka_cherez_epk = data['zayavka_cherez_epk'], 
 novyiy_klient = data['novyiy_klient']
  )

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

































