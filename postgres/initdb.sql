-- Check if the database exists and create it if not
-- This block uses a trick with DO $$ ... $$ to run PL/pgSQL
-- which allows conditional logic
DO
$do$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'olympic_db') THEN
       CREATE DATABASE olympic_db;
    END IF;
END
$do$;


-- Création de table pour le jeu de données
CREATE TABLE IF NOT EXISTS fact_resultats_epreuves (
    id_resultat  INTEGER NOT NULL,
    id_resultat_source INTEGER NOT NULL,
    source VARCHAR,
    id_athlete_base_resultats  VARCHAR,
    id_personne  VARCHAR,
    athlete_nom  VARCHAR,
    athlete_prenom  VARCHAR,
    id_equipe  INTEGER,
    equipe_en  VARCHAR,
    id_pays  INTEGER,
    pays_en_base_resultats  VARCHAR,
    classement_epreuve  VARCHAR,
    performance_finale_texte  VARCHAR,
    performance_finale  VARCHAR,
    id_evenement  INTEGER,
    evenement  VARCHAR,
    evenement_en  VARCHAR,
    categorie_age  VARCHAR,
    id_edition  INTEGER,
    id_competition_sport  INTEGER,
    competition_en  VARCHAR,
    id_type_competition  INTEGER,
    type_competition  VARCHAR,
    edition_saison  INTEGER,
    date_debut_edition  VARCHAR,
    date_fin_edition  VARCHAR,
    id_ville_edition  INTEGER,
    edition_ville_en  VARCHAR,
    id_nation_edition_base_resultats  INTEGER,
    edition_nation_en  VARCHAR,
    id_sport  INTEGER,
    sport  VARCHAR,
    sport_en  VARCHAR,
    id_discipline_administrative  INTEGER,
    discipline_administrative  VARCHAR,
    id_specialite  INTEGER,
    specialite  VARCHAR,
    id_epreuve  INTEGER,
    epreuve  VARCHAR,
    epreuve_genre  VARCHAR,
    epreuve_type  VARCHAR,
    est_epreuve_individuelle  INTEGER,
    est_epreuve_olympique  INTEGER,
    est_epreuve_ete  INTEGER,
    est_epreuve_handi  INTEGER,
    epreuve_sens_resultat  INTEGER,
    id_federation  INTEGER,
    federation  VARCHAR,
    federation_nom_court  VARCHAR,
    dt_creation  VARCHAR,
    dt_modification  VARCHAR
);