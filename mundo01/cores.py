
class Cores:
    def __init__(self):
        self.fontCores = {'preto': '\033[7;30m'}
        self.backgroundCores = {}
        self.criarcores()

    def criarcores(self):
        cores = ['branco', 'vermelho', 'verde', 'amarelo', 'azul', 'roxo', 'verde-escuro', 'cinza']

        for i in range(0, 8):
            self.fontCores[cores[i]] = f'\033[{i+30}m'
            self.backgroundCores[cores[i]] = f'\033[{i+40}m'

    def font(self, cor):
        return self.fontCores[cor]

    def background(self, cor):
        return self.backgroundCores[cor]

    def limpar(self):
        return '\033[m'
