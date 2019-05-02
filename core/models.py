from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    lancamento = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + ' - ' + self.autor
