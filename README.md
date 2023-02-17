# :pushpin: Projet DevOps Bachelor

Projet réalisé dans le cadre des cours DevOps en Bachelor.

- [:pushpin: Projet DevOps Bachelor](#pushpin-projet-devops-bachelor)
  - [Concept](#concept)
  - [Tester en local](#tester-en-local)
  - [CI/CD](#cicd)

## Concept

:warning: In progress

Frontend Angular qui accède à une base de donnée MongoDB via une API RESTFull codée en Python/Flask. Ce repo contient les informations de déploiement sur un cloud AWS de l'ensemble du code via GitHub Action.

**UP** Le déploiement sur AWS fonctionne désormais via le template cloudformation.

## Tester en local

```bash
git clone https://github.com/fabienchevalier/fabien-aws-sdv.git
cd fabien-aws-sdv/b
git checkout master
docker-compose up
```

Ce qui donnera :

- Un front-end accessible via http://localhost:8090
- Une api backend accessible via http://localhost:8080/api/v1
- Une DB MongoDB containeurisée qui communique avec le backend via PyMongo accessible sur http://localhost:27017
- Une interface web pour la base mongo db dispo sur http://localhost:8081 (pour tester)

## CI/CD

Teste le fonctionnement du backend dans le runner, puis déploie l'infrastructure dans une machine AWS EC2 via le template CloudFormation. 

