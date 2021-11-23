# Generated by Django 3.2.7 on 2021-09-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0165_ticketcategorywsprotocollo_protocollo_uo_rpa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticketcategorywsprotocollo",
            name="protocollo_uo",
            field=models.CharField(
                choices=[
                    ("2015.1", "AMMINISTRAZIONE CTC"),
                    ("2013.1", "AMMINISTRAZIONE DEMACS"),
                    ("2025.1", "AMMINISTRAZIONE DESF"),
                    ("2020.1", "AMMINISTRAZIONE DIAM"),
                    ("2014.1", "AMMINISTRAZIONE DIBEST"),
                    ("2022.1", "AMMINISTRAZIONE DICES"),
                    ("2019.1", "AMMINISTRAZIONE DIMEG"),
                    ("2017.1", "AMMINISTRAZIONE DIMES"),
                    ("2018.1", "AMMINISTRAZIONE DINCI"),
                    ("2024.1", "AMMINISTRAZIONE DISCAG"),
                    ("2023.1", "AMMINISTRAZIONE DISU"),
                    ("2021.1", "AMMINISTRAZIONE FARMACIA"),
                    ("2016.1", "AMMINISTRAZIONE FISICA"),
                    ("2026.1", "AMMINISTRAZIONE SPES"),
                    ("2079.2", "AREA AFFARI GENERALI"),
                    ("0012.1", "AREA BILANCIO E CICLO ATTIVO"),
                    ("0019.3", "AREA DIRITTO ALLO STUDIO"),
                    ("2080.4", "AREA EDILIZIA, VIABILITA' ED ESPROPRI"),
                    ("0012.2", "AREA FISCALE E CICLO PASSIVO"),
                    ("2079.3", "AREA GARE D'APPALTO"),
                    ("2080.3", "AREA IMPIANTI"),
                    (
                        "2032.1",
                        "AREA INFRASTRUTTURE INFORMATICHE E DI TELECOMUNICAZIONE",
                    ),
                    ("917.3", "AREA INTERNALIZZAZIONE"),
                    ("917.1", "AREA OFFERTA FORMATIVA"),
                    ("917.4", "AREA ORIENTAMENTO, INCLUSIONE E CAREER SERVICE"),
                    (
                        "896.4",
                        "AREA PERSONALE CONTRATTUALIZZATO E COLLABORATORI ESTERNI",
                    ),
                    ("2066", "AREA POST-LAUREA"),
                    ("896.3", "AREA PROFESSORI E RICERCATORI"),
                    ("896.5", "AREA RELAZIONI SINDACALI E SVILUPPO ORGANIZZATIVO"),
                    ("0019.4", "AREA RESIDENZIALITA'"),
                    ("907", "AREA RICERCA INNOVAZIONE E IMPATTO SOCIALE"),
                    ("2032.3", "AREA SERVIZI DI SUPPORTO E HELPDESK"),
                    ("917.2", "AREA SERVIZI DIDATTICI"),
                    ("2079.4", "AREA SERVIZI GENERALI"),
                    ("2032.2", "AREA SISTEMI INFORMATIVI"),
                    ("0019.5", "AREA SOCIALITA' E SALE CONVEGNI"),
                    ("1.5", "AVVOCATURA D'ATENEO"),
                    ("640", "CENTRO ARTI MUSICA E SPETTACOLO"),
                    ("1790", "CENTRO EDITORIALE E LIBRARIO"),
                    ("1600", "CENTRO LINGUISTICO DI ATENEO"),
                    ("1860", "CENTRO SANITARIO"),
                    ("SI000017", "COMITATO ETICO DI ATENEO"),
                    ("SI000018", "COMITATO UNICO DI GARANZIA"),
                    ("2015.2", "DIDATTICA CTC"),
                    ("2013.2", "DIDATTICA DEMACS"),
                    ("2025.2", "DIDATTICA DESF"),
                    ("2020.2", "DIDATTICA DIAM"),
                    ("2014.2", "DIDATTICA DIBEST"),
                    ("2022.2", "DIDATTICA DICES"),
                    ("2019.2", "DIDATTICA DIMEG"),
                    ("2017.2", "DIDATTICA DIMES"),
                    ("2018.2", "DIDATTICA DINCI"),
                    ("2024.2", "DIDATTICA DISCAG"),
                    ("2023.2", "DIDATTICA DISU"),
                    ("2021.2", "DIDATTICA FARMACIA"),
                    ("2016.2", "DIDATTICA FISICA"),
                    ("2026.2", "DIDATTICA SPES"),
                    (
                        "2014",
                        "DIPARTIMENTO DI BIOLOGIA, ECOLOGIA E SCIENZE DELLA TERRA",
                    ),
                    ("2015", "DIPARTIMENTO DI CHIMICA E TECNOLOGIE CHIMICHE"),
                    ("2022", "DIPARTIMENTO DI CULTURE EDUCAZIONE SOCIETA'"),
                    ("2025", "DIPARTIMENTO DI ECONOMIA STATISTICA E FINANZA"),
                    ("2021", "DIPARTIMENTO DI FARMACIA"),
                    ("2016", "DIPARTIMENTO DI FISICA"),
                    ("2018", "DIPARTIMENTO DI INGEGNERIA CIVILE"),
                    ("2020", "DIPARTIMENTO DI INGEGNERIA DELL'AMBIENTE"),
                    (
                        "2017",
                        "DIPARTIMENTO DI INGEGNERIA INFORMATICA MODELLISTICA ELETTRONICA E SISTEMISTICA",
                    ),
                    (
                        "2019",
                        "DIPARTIMENTO DI INGEGNERIA MECCANICA ENERGETICA E GESTIONALE",
                    ),
                    ("2013", "DIPARTIMENTO DI MATEMATICA E INFORMATICA"),
                    ("2024", "DIPARTIMENTO DI SCIENZE AZIENDALI GIURIDICHE"),
                    ("2023", "DIPARTIMENTO DI STUDI UMANISTICI"),
                    ("2026", "DIPARTIMENTO SCIENZE POLITICHE SOCIALI"),
                    ("2079", "DIREZIONE AFFARI GENERALI E ATTIVITA' NEGOZIALE"),
                    ("19", "DIREZIONE CENTRO RESIDENZIALE"),
                    ("12", "DIREZIONE FINANZIARIA"),
                    ("1", "DIREZIONE GENERALE"),
                    ("896", "DIREZIONE RISORSE UMANE"),
                    ("2080", "DIREZIONE TECNICA E PATRIMONIO IMMOBILIARE"),
                    ("SI000006", "LABORATORIO ALBANOLOGIA"),
                    ("SI000005", "LABORATORIO FONETICA"),
                    ("SI000004", "LABORATORIO LABDOC"),
                    ("917", "MACRO AREA DIDATTICA E SERVIZI AGLI STUDENTI"),
                    ("2032", "MACRO AREA SERVIZI INFORMATICI E TECNOLOGICI"),
                    ("1750", "MUSEO DI STORIA NATURALE ED ORTO BOTANICO"),
                    ("SI000022", "POLO DI INFANZIA"),
                    ("1740", "POLO ECONOMICO GIURIDICO"),
                    ("1760", "POLO SCIENTIFICO"),
                    ("1820", "POLO UMANISTICO"),
                    ("2015.3", "RICERCA CTC"),
                    ("2013.3", "RICERCA DEMACS"),
                    ("2025.3", "RICERCA DESF"),
                    ("2020.3", "RICERCA DIAM"),
                    ("2014.3", "RICERCA DIBEST"),
                    ("2022.3", "RICERCA DICES"),
                    ("2019.3", "RICERCA DIMEG"),
                    ("2017.3", "RICERCA DIMES"),
                    ("2018.3", "RICERCA DINCI"),
                    ("2024.3", "RICERCA DISCAG"),
                    ("2023.3", "RICERCA DISU"),
                    ("2021.3", "RICERCA FARMACIA"),
                    ("2016.3", "RICERCA FISICA"),
                    ("2026.3", "RICERCA SPES"),
                    ("2012", "RIMUSEUM - MUSEO PER L'AMBIENTE"),
                    ("SI000020", "RPCT"),
                    ("2026.4", "SCUOLA SUPERIORE DI SCIENZE DELLE AMM.NI PUBBLICHE"),
                    ("1.3", "SEGRETERIA DEL RETTORE"),
                    ("1.4", "SEGRETERIA ORGANI DI GOVERNO"),
                    ("SI000014", "Segreteria Studenti DIMEG"),
                    ("SI000015", "SERVIZI DIMEG"),
                    ("1840.3", "SERVIZIO AMMINISTRATIVO"),
                    ("0019.2", "SERVIZIO AMMINISTRATIVO CR"),
                    ("2079.1", "SERVIZIO ANTICORRUZIONE E LEGALITA'"),
                    ("1840.1", "SERVIZIO AUTOMAZIONE BIBLIOTECHE"),
                    ("1.2", "SERVIZIO COMUNICAZIONE"),
                    ("1.6", "SERVIZIO DI PREVENZIONE E PROTEZIONE"),
                    ("2080.2", "SERVIZIO ENERGY MANAGEMENT"),
                    ("1840.2", "SERVIZIO LOGISTICO"),
                    ("1.7", "SERVIZIO MONITORAGGIO, QUALITA' E VALUTAZIONE"),
                    ("1.1", "SERVIZIO PROGETTI INFRASTRUTTURE"),
                    ("896.2", "SERVIZIO PROGRAMMAZIONE E MONITORAGGIO"),
                    ("2080.1", "SERVIZIO QUALITA' E FACILITY MANAGEMENT"),
                    ("SI000002", "Servizio Ricezione Pec"),
                    ("0019.1", "SERVIZIO SISTEMI INFORMATIVI"),
                    ("896.1", "SERVIZIO TRATTAMENTO PREVIDENZIALE"),
                    ("0012.1A", "SETTORE BILANCIO"),
                    ("0012.1B", "SETTORE CICLO ATTIVO"),
                    ("0012.2B", "SETTORE CICLO PASSICO"),
                    ("2066.1", "SETTORE DOTTORATI DI RICERCA"),
                    ("0012.2A", "SETTORE EMOLUMENTI E FISCALE"),
                    ("2066.3", "SETTORE FORMAZIONE INSEGNANTI ED ESAMI DI STATO"),
                    ("2079.2A", "SETTORE GESTIONE DOCUMENTALE E PRIVACY"),
                    ("0019.4A", "SETTORE GESTIONE RESIDENZE"),
                    ("907.2", "SETTORE INNOVAZIONE E IMPATTO SOCIALE"),
                    ("2066.2", "SETTORE MASTER E CORSI POST LAUREA"),
                    ("1.7B", "SETTORE MONITORAGGIO PERFORMANCE"),
                    ("2032.1A", "SETTORE RETI E SICUREZZA"),
                    ("907.1", "SETTORE RICERCA"),
                    ("1740.1", "SETTORE RISORSE BIBLIOGRAFICHE"),
                    ("1760.1", "SETTORE RISORSE BIBLIOGRAFICHE"),
                    ("1820.1", "SETTORE RISORSE BIBLIOGRAFICHE"),
                    ("1740.2", "SETTORE SERVIZI AL PUBBLICO"),
                    ("1760.2", "SETTORE SERVIZI AL PUBBLICO"),
                    ("1820.2", "SETTORE SERVIZI AL PUBBLICO"),
                    ("2032.2B", "SETTORE SI AMMINISTRATIVI E DOCUMENTALI"),
                    ("2032.2A", "SETTORE SI PER RICERCA E DIDATTICA"),
                    ("2032.1B", "SETTORE SISTEMI E CLOUD"),
                    ("1.7C", "SETTORE STATISTICHE E REPORTING"),
                    ("0019.4B", "SETTORE TECNICO"),
                    ("2032.1C", "SETTORE TELEFONIA"),
                    ("1.7A", "SETTORE VALUTAZIONE E QUALITA'"),
                    ("1840", "SISTEMA BIBLIOTECARIO DI ATENEO"),
                    ("SI000012", "TECNICA DIMES"),
                    ("SI000003", "TECNICA ELABORAZIONE DATI DICES"),
                    ("0", "UNIVERSITA' DELLA CALABRIA"),
                ],
                max_length=12,
                verbose_name="UO",
            ),
        ),
    ]
