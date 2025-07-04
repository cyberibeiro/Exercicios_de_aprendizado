'''Introdução
O ano é 2525 e você acaba de embarcar em uma jornada para visitar todos os planetas do Sistema Solar (Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano e Netuno). A primeira parada é Mercúrio, onde a alfândega exige que você preencha um formulário (a burocracia aparentemente não é específica da Terra). Quando você entrega o formulário ao funcionário da alfândega, ele o examina e franze a testa. "Você realmente espera que eu acredite que você tem apenas 50 anos? Você deve estar mais perto de 200 anos!"

Divertido, você espera que o funcionário da alfândega comece a rir, mas eles parecem estar falando sério. Você percebe que entrou na sua idade em anos terrestres, mas o oficial esperava isso nos anos de Mercúrio! Como o período orbital de Mercúrio ao redor do sol é significativamente mais curto do que a Terra, você é muito mais velho nos anos de Mercúrio. Após alguns cálculos rápidos, você pode fornecer sua idade em anos de mercúrio. O funcionário da alfândega sorri, satisfeito, e acena para você. Você faz uma anotação mental para pré-calcular sua idade específica do planeta antes de futuras verificações alfandegárias, para evitar tais confusões.

Nota
Se você está se perguntando por que Plutão não fez o corte, assista a este vídeo do YouTube.

Instruções
Dada uma idade em segundos, calcule quantos anos alguém teria em um planeta em nosso Sistema Solar.

Um ano terrestre equivale a 365,25 dias terrestres, ou 31.557.600 segundos. Se lhe dissessem que alguém tinha 1.000.000.000 de segundos de idade, sua idade seria de 31,69 anos terrestres.

Para os outros planetas, você deve levar em conta seu período orbital em Anos Terrestres:

Planeta	Período orbital em anos terrestres
Mercúrio	0.2408467
Vênus	0.61519726
Terra	1.0
Marte	1.8808158
Júpiter	11.862615
Saturno	29.447498
Urano	84.016846
Netuno	164.79132
Nota
O comprimento real de uma órbita completa da Terra ao redor do sol está mais próximo de 365.256 dias (1 ano sideral). O calendário gregoriano tem, em média, 365,2425 dias. Embora não seja totalmente preciso, 365,25 é o valor usado neste exercício. Veja Ano na Wikipedia para mais maneiras de medir um ano.

Para a trilha Python, este exercício pede que você crie uma classe (classes) que inclua métodos para todos os planetas do sistema solar. Os métodos devem seguir a convenção de nomenclatura .SpaceAgeon_<planet name>

Cada método deve ter a idade ("no" planeta) em anos, arredondada para duas casas decimais:return

#creating an instance with one billion seconds, and calling .on_earth().
>>> SpaceAge(1000000000).on_earth()

#This is one billion seconds on Earth in years
31.69
Para obter mais informações sobre como construir e usar classes, consulte:

Uma primeira olhada nas classes da documentação do Python.
Uma palavra sobre nomes e objetos da documentação do Python.
Objetos, valores e tipos na documentação do modelo de dados do Python.
O que é uma classe? do site Trey Hunners Python Morsels.'''