# :pushpin: Projet DevOps angular/python

```bash
git clone https://github.com/fabienchevalier/fabien-aws-sdv.git
cd fabien-aws-sdv/b
git checkout master
docker-compose up
```

- Un front-end accessible via http://localhost:8090
- Une api backend accessible via http://localhost:8080/api/v1
- Une DB MongoDB containeurisée qui communique avec le backend via pymongo
- Une interface web pour la base mongo db dispo sur http://localhost:8081

# CI/CD

A chaque push, l'API est testée via un script uni_test.py, executé dans GitHub action. Si les tests sont OK, le backend est déployé dans la branche DEV. 