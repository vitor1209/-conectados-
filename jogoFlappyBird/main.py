import pygame
import os
import random

TelaAltura = 800
TelaLargura = 500

imgCano = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
imgFundo = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
imgChao = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
imgPassaro = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()
FontePontos = pygame.font.SysFont('arial', 50)

class Passaro:
    imgs = imgPassaro
    RotacaoMaxima = 25
    VelocidadeRodacao = 20
    TempoAnimacao = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagemImagem = 0
        self.imagem = self.imgs[0]

    def Pular(self):
        self.velocidade = -12
        self.tempo = 0
        self.altura = self.y
        
    def mover(self):
        self.tempo += 1
        deslocamento = self.velocidade * self.tempo + 1.5 * self.tempo**2

        if deslocamento >= 16:
            deslocamento = 14
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.RotacaoMaxima:
                self.angulo = self.RotacaoMaxima
        else:
            if self.angulo > -90:
                self.angulo -= self.VelocidadeRodacao

    def desenhar(self, tela):
        self.contagemImagem += 1

        if self.contagemImagem < self.TempoAnimacao:
            self.imagem = self.imgs[0]
        elif self.contagemImagem < self.TempoAnimacao * 2:
            self.imagem = self.imgs[1]
        elif self.contagemImagem < self.TempoAnimacao * 3:
            self.imagem = self.imgs[2]
        elif self.contagemImagem >= self.TempoAnimacao * 4:
            self.imagem = self.imgs[0]
            self.contagemImagem = 0

        if self.angulo <= -80:
            self.imagem = self.imgs[1]
            self.contagemImagem = self.TempoAnimacao * 2

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        nova_posicao = imagem_rotacionada.get_rect(center=self.imagem.get_rect(topleft=(self.x, self.y)).center)
        tela.blit(imagem_rotacionada, nova_posicao.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Cano:
    Distancia = 280
    Velocidade = 3

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.posTopo = 0
        self.posBase = 0
        self.canoTopo = pygame.transform.flip(imgCano, False, True)
        self.canoBase = imgCano
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.posTopo = self.altura - self.canoTopo.get_height()
        self.posBase = self.altura + self.Distancia

    def mover(self):
        self.x -= self.Velocidade

    def desenhar(self, tela):
        tela.blit(self.canoTopo, (self.x, self.posTopo))
        tela.blit(self.canoBase, (self.x, self.posBase))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.canoTopo)
        base_mask = pygame.mask.from_surface(self.canoBase)

        distancia_topo = (self.x - passaro.x, self.posTopo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.posBase - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if topo_ponto or base_ponto:
            return True

        return False


class Chao:
    Velocidade = 3
    Largura = imgChao.get_width()
    Imagem = imgChao

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.Largura

    def mover(self):
        self.x1 -= self.Velocidade
        self.x2 -= self.Velocidade

        if self.x1 + self.Largura < 0:
            self.x1 = self.x2 + self.Largura

        if self.x2 + self.Largura < 0:
            self.x2 = self.x1 + self.Largura

    def desenhar(self, tela):
        tela.blit(self.Imagem, (self.x1, self.y))
        tela.blit(self.Imagem, (self.x2, self.y))


def desenharTela(tela, passaros, canos, chao, pontos):
    tela.blit(imgFundo, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)

    for cano in canos:
        cano.desenhar(tela)

    texto = FontePontos.render(f"Pontuação: {pontos}", True, (255, 255, 255))
    tela.blit(texto, (TelaLargura - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()


def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TelaLargura, TelaAltura))
    pontos = 0
    relogio = pygame.time.Clock()
    
    iniciado = False  # Variável para verificar se o jogo já começou

    rodando = True
    while rodando:
        relogio.tick(30)
        # interação
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    if not iniciado:
                        iniciado = True  # O jogo começa após o primeiro clique
                    for passaro in passaros:
                        passaro.Pular()

        if not iniciado:
            desenharTela(tela, passaros, canos, chao, pontos)
            continue  # Continua exibindo a tela inicial até que o jogo comece

        # mover
        for passaro in passaros:
            passaro.mover()
        chao.mover()

        adicionarCano = False
        removerCanos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionarCano = True
            cano.mover()
            if cano.x + cano.canoTopo.get_width() < 0:
                removerCanos.append(cano)

        if adicionarCano:
            pontos += 1
            canos.append(Cano(600))

        for cano in removerCanos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                passaros.pop(i)

        if pontos > 3 :
            Chao.Velocidade = 3.5
            Cano.Velocidade = 3.5
            Cano.Distancia = 260
        
        if pontos > 5 :
            Chao.Velocidade = 4
            Cano.Velocidade = 4
            Cano.Distancia = 240

        if pontos > 8 :
            Chao.Velocidade = 4.5
            Cano.Velocidade = 4.5
            Cano.Distancia = 220
        
        if pontos > 10 :
            Chao.Velocidade = 5
            Cano.Velocidade = 5
            Cano.Distancia = 200

        if pontos > 12 :
            Chao.Velocidade = 5.5
            Cano.Velocidade = 5.5
             
        if pontos > 15 :
            Chao.Velocidade = 6
            Cano.Velocidade = 6
            Cano.Distancia = 190

        desenharTela(tela, passaros, canos, chao, pontos)



if __name__ == '__main__':
    main()
