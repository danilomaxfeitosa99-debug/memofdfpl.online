#!/usr/bin/env python3
"""Batch replace all remaining English text in index.html for AuraVita rebrand."""

import re

FILE = '/home/ettym/Documentos/GitHub/neurozoom_clone/index.html'

with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# ============ WARNING SECTION ============
html = html.replace(
    '<strong>WARNING</strong>:  Auravitais',
    '<strong>ADVERTENCIA</strong>: AuraVita'
).replace(
    '<strong>NOT</strong> sold in stores or elsewhere online and never will be.',
    '<strong>NO</strong> se vende en tiendas ni en otros sitios web y nunca se venderá.'
).replace(
    '<div>It is\n                                    only available for purchase on this page <strong>ONLY</strong>.</div>',
    '<div>Solo está disponible para compra en esta página <strong>SOLAMENTE</strong>.</div>'
).replace(
    "<div>In fact, this is the very last time you'll ever be able to get Neurozoom.</div>",
    '<div>De hecho, esta es la última oportunidad que tendrás de obtener AuraVita.</div>'
).replace(
    '<div>Act now to fully support your memory and cognitive health now and well into the\n                                    future.</div>',
    '<div>Actúa ahora para apoyar completamente tu memoria y tu salud cognitiva hoy y en el futuro.</div>'
)

# ============ REFUND POLICY SECTION ============
html = html.replace(
    '<strong>Refund Policy</strong>',
    '<strong>Política de Reembolso</strong>'
).replace(
    "<strong>Your Satisfaction is our #1\n                                priority</strong>",
    '<strong>Tu satisfacción es nuestra prioridad #1</strong>'
).replace(
    "We are so confident you'll <b>enjoy life-changing results</b> that we're prepared to back up\n                             Auravitawith a 100% satisfaction guarantee for the next 60 days.",
    'Estamos tan seguros de que <b>disfrutarás resultados que cambiarán tu vida</b> que estamos dispuestos a respaldar AuraVita con una garantía de satisfacción del 100% durante los próximos 60 días.'
).replace(
    "If you are not absolutely astounded by the results, then we will only be too happy to refund\n                            you every cent. No questions asked. It's time to get in the driver's seat and be in control\n                            of your health again.",
    'Si no quedas absolutamente asombrado por los resultados, con gusto te reembolsaremos cada centavo. Sin preguntas. Es hora de tomar el control de tu salud de nuevo.'
).replace(
    'If you are unhappy with Neurozoom, simply return it within <b>60 days</b> of receiving it and\n                            we\'ll give you a full refund. It\'s that simple.',
    'Si no estás satisfecho con AuraVita, simplemente devuélvelo dentro de <b>60 días</b> de haberlo recibido y te daremos un reembolso completo. Así de simple.'
)

# ============ FAQ SECTION ============
html = html.replace(
    '<strong>Do you have questions? We have\n                                answers!&nbsp;</strong>',
    '<strong>¿Tienes preguntas? ¡Tenemos respuestas!</strong>'
)

# FAQ Q1
html = html.replace(
    'Will  Auravitawork for me?',
    '¿AuraVita funcionará para mí?'
).replace(
    'We put a lot of work and passion\n                                        into creating this product, and thousands of satisfied customers really stand by\n                                        it. <br>As with all natural solutions, we recommend giving  Auravitaa fair\n                                        chance, in order for all the potent ingredients to activate and be absorbed by\n                                        your body.',
    'Hemos invertido mucho trabajo y pasión en la creación de este producto, y miles de clientes satisfechos lo respaldan. <br>Como con todas las soluciones naturales, recomendamos dar a AuraVita una oportunidad justa, para que todos los ingredientes potentes se activen y sean absorbidos por tu cuerpo.'
)

# FAQ Q2
html = html.replace(
    'Is  Auravitareally safe\n                                        ?&nbsp;',
    '¿AuraVita es realmente seguro?'
).replace(
    'We take exceptional pride in our\n                                        products and in their safety. <br>Even so, we recommended that if you have any\n                                        prior concerns, first check with a medical professional before including any\n                                        dietary supplement into your diet routine, especially when taking other\n                                        medications. <br>You should also know that each bottle your order is sealed by\n                                        the producer\'s medical laboratory, guaranteeing all safety measurements a\n                                        medical facility must offer. <br>Moreover, the bottles you have purchased will\n                                        arrive at your delivery address properly packed by our trusted shipping\n                                        company.<br>',
    'Nos enorgullecemos enormemente de nuestros productos y de su seguridad. <br>Aun así, recomendamos que si tienes alguna preocupación previa, consultes primero con un profesional médico antes de incluir cualquier suplemento dietético en tu rutina, especialmente si estás tomando otros medicamentos. <br>También debes saber que cada botella de tu pedido está sellada por el laboratorio médico del fabricante, garantizando todas las medidas de seguridad que una instalación médica debe ofrecer. <br>Además, las botellas que has comprado llegarán a tu dirección de entrega correctamente empaquetadas por nuestra empresa de envíos de confianza.<br>'
)

# FAQ Q3
html = html.replace(
    'How long would it take to\n                                        receive the product to my delivery address?',
    '¿Cuánto tiempo tardaría en recibir el producto en mi dirección de entrega?'
).replace(
    'Lately, we have been flooded with orders from all over the world! Even so, we\n                                        strive to ship your order in maximum <strong>24h </strong>each working day of\n                                        the week. To make things easy, you will receive an email with your tracking\n                                        number so that you can follow your package on route to its destination. On\n                                        average, customers reported the real shipping time is somewhere between 5 to 10\n                                        days for domestic orders.',
    'Últimamente, ¡hemos recibido pedidos de todo el mundo! Aun así, nos esforzamos por enviar tu pedido en un máximo de <strong>24h</strong> cada día laborable de la semana. Para facilitar las cosas, recibirás un correo electrónico con tu número de seguimiento para que puedas rastrear tu paquete hasta su destino. En promedio, los clientes reportan un tiempo de envío real de entre 5 y 10 días para pedidos nacionales.'
)

# FAQ Q4
html = html.replace(
    'How will I identify the\n                                         transaction on my bank statement?',
    '¿Cómo identificaré la transacción en mi estado de cuenta bancario?'
).replace(
    'Your purchase will appear on your\n                                        bank statement under the name of "xxxxx\u201d. We care about the confidentiality of\n                                        your purchase and so we will never reveal to anyone the content of your order,\n                                        so the supplement name will not be mentioned anywhere else besides the delivered\n                                        package.<br>',
    'Tu compra aparecerá en tu estado de cuenta bancario bajo el nombre de "xxxxx". Nos preocupamos por la confidencialidad de tu compra y nunca revelaremos a nadie el contenido de tu pedido, por lo que el nombre del suplemento no se mencionará en ningún otro lugar aparte del paquete entregado.<br>'
)

# FAQ Q5
html = html.replace(
    'Is there a refund policy for\n                                        my transaction?',
    '¿Existe una política de reembolso para mi transacción?'
)
# The answer for Q5 is complex with email links, replace the core text
html = html.replace(
    'Yes. Your investment is completely protected by the 60-Day 100% Money-Back\n                                        Guarantee. This means that for the next 2 full months after your purchase, if\n                                        you are not happy with or you simply changed your mind, you have every right to\n                                        ask for your money back. For any inquiries, please contact us at',
    'Sí. Tu inversión está completamente protegida por la Garantía de Devolución del 100% del Dinero en 60 Días. Esto significa que durante los próximos 2 meses completos después de tu compra, si no estás satisfecho o simplemente cambiaste de opinión, tienes todo el derecho de pedir la devolución de tu dinero. Para cualquier consulta, contáctanos en'
).replace(
    'Be noticed that you will be required to ship the product bottle(s) back to us\n                                        at:',
    'Ten en cuenta que se te pedirá que envíes las botellas del producto de vuelta a:'
).replace(
    'for the refund to\n                                        be approved.',
    'para que el reembolso sea aprobado.'
)

# FAQ Q6
html = html.replace(
    'Does your product require\n                                        multiple payments?',
    '¿Su producto requiere múltiples pagos?'
).replace(
    'Absolutely not. To purchase Neurozoom, you are only asked for a one-time\n                                        payment, right on this page. There are no other future payments needed to\n                                        benefit from this product.',
    'Absolutamente no. Para comprar AuraVita, solo se te pide un pago único, aquí mismo en esta página. No se necesitan otros pagos futuros para beneficiarte de este producto.'
)

# FAQ Q7
html = html.replace(
    'How secure are this page and\n                                        my transaction?',
    '¿Qué tan segura es esta página y mi transacción?'
).replace(
    'This website is highly secure. We use industry-leading technology (such as SSL)\n                                        to keep your information 100% safe.',
    'Este sitio web es altamente seguro. Utilizamos tecnología líder en la industria (como SSL) para mantener tu información 100% segura.'
)

# FAQ Q8
html = html.replace(
    'I have additional questions.\n                                         Can you help me out?',
    '¿Tengo preguntas adicionales. ¿Pueden ayudarme?'
).replace(
    'We always welcome any questions coming from you. You can always find one of our\n                                        "customer satisfaction fanatics", by writing us at',
    'Siempre damos la bienvenida a cualquier pregunta. Puedes encontrar a uno de nuestros "fanáticos de la satisfacción del cliente" escribiéndonos a'
)

# ============ REMAINING  Auravita→ AuraVita / Auravita replacements ============
html = html.replace('Neurozoom', 'AuraVita')
html = html.replace('NeuroZoom', 'AuraVita')
html = html.replace('neurozoom', 'auravita')

# ============ FOOTER TRANSLATIONS ============
html = html.replace(
    'The content of this site is for informational purposes only and is not intended to provide any financial, legal, medical or tax advice. You should consult an appropriate professional for advice specific to your situation.',
    'El contenido de este sitio es solo con fines informativos y no pretende proporcionar ningún consejo financiero, legal, médico o fiscal. Debes consultar a un profesional apropiado para obtener asesoramiento específico para tu situación.'
)
html = html.replace(
    'This site is not a part of the Facebook/Meta website or Facebook Inc, nor the Google Website or Alphabet Inc.',
    'Este sitio no forma parte del sitio web de Facebook/Meta ni de Facebook Inc, ni del sitio web de Google ni de Alphabet Inc.'
)
html = html.replace(
    'Additionally, This site is NOT endorsed by Facebook/Meta or Google in any way.',
    'Además, este sitio NO está respaldado por Facebook/Meta ni por Google de ninguna manera.'
)
html = html.replace(
    'FACEBOOK is a trademark of FACEBOOK, Inc. YOUTUBE and GOOGLE are trademarks of ALPHABET, Inc.',
    'FACEBOOK es una marca comercial de FACEBOOK, Inc. YOUTUBE y GOOGLE son marcas comerciales de ALPHABET, Inc.'
)
html = html.replace(
    'Results may not be typical and may vary from person to person.',
    'Los resultados pueden no ser típicos y pueden variar de persona a persona.'
)
html = html.replace(
    'Making a purchase through any of our links may result in a commission for us. Please be aware that',
    'Realizar una compra a través de cualquiera de nuestros enlaces puede generar una comisión para nosotros. Ten en cuenta que'
)

# Remove ClickBank support references
html = html.replace(
    'For Product Support, please contact the vendor <a href="https://www.clkbank.com/#!/">HERE</a>.',
    ''
).replace(
    'For Order Support, please contact ClickBank <a href="https://www.clkbank.com/#!/">HERE</a>.',
    ''
)

# ============ SCIENTIFIC REFERENCES SECTION — REMOVE ============
# Find and remove the entire scientific references section
ref_pattern = re.compile(
    r'<section[^>]*class="[^"]*ref-bg[^"]*"[^>]*>.*?</section>',
    re.DOTALL
)
html = ref_pattern.sub('<!-- Scientific references section removed -->', html)

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ All remaining translations applied successfully!")
