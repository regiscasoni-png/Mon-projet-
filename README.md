# Prospection locale quotidienne — Digit Formations

Kit de prospection basé sur le catalogue Digit Formations (6 formations certifiantes,
finançables CPF ou entreprise, 1 650 € / 2 000 €).

## Fonctionnement quotidien

Chaque jour, tu m'indiques **la zone du jour** (commune + rayon, ex. « aujourd'hui je suis
vers Vitrolles, 15 km »). Je produis en retour une liste de prospects qualifiés dans
`prospects/AAAA-MM-JJ-zone.md` :

1. **Recherche des entreprises locales** correspondant aux profils cibles
   (voir `ciblage/profils-cibles.md`) : artisans, commerçants, indépendants,
   professions libérales, TPE de services.
2. **Priorisation** selon les signaux d'achat : pas de site web, site vieillissant,
   réseaux sociaux inactifs, avis Google peu nombreux, activité récemment créée.
3. **Association formation ↔ prospect** : pour chaque prospect, la ou les formations
   du catalogue à proposer et l'angle d'approche.
4. **Coordonnées** : téléphone/adresse publics ; dirigeant identifié quand c'est possible.

## Structure du dépôt

- `ciblage/profils-cibles.md` — qui viser, pour quelle formation, avec quels signaux
- `ciblage/argumentaires.md` — angles d'approche et réponses aux objections
- `modeles/messages.md` — scripts d'appel, messages LinkedIn et e-mails types
- `prospects/` — les listes quotidiennes, une par jour et par zone

## Sources utilisées

- Recherche web (fiches Google, Pages Jaunes, sites locaux, annuaires métiers)
- RocketReach (identification des dirigeants — compte gratuit, quota limité :
  ~50 recherches/mois, à réserver aux meilleurs prospects)
- Registre National des Entreprises via l'outil infosociétés (vérification SIREN,
  forme juridique, date de création)
