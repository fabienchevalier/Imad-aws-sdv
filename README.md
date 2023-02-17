# Projet DevOps angular/python

Test local :

```bash
git clone https://github.com/fabienchevalier/fabien-aws-sdv.git
cd fabien-aws-sdv && checkout master
docker-compose up
```

## Principe

- Un front-end accessible via http://serverip:8090
- Une api backend accessible via http://serverip:8080/api/v1
- Une DB MongoDB containeurisée qui communique avec le backend via pymongo
- Une interface web pour la base mongo db dispo sur http://serverip:8081

## CI/CD

2 jobs:

- Build test:
  - Teste l'api dans le runner GitHub pour garantir son fonctionnement
- Deploy to aws:
  - Deploie l'infrastructure sur le cloud AWS via un template CloudFormation
