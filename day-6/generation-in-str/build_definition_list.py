def build_definition_list(definitions):
    if not definitions:
        return ''
    items = ''.join(f'<dt>{term}</dt><dd>{description}</dd>' for term, description in definitions)
    return f'<dl>{items}</dl>' 


definitions = [
    ['Блямба', 'Выпуклость, утолщение на поверхности чего-либо'],
    ['Бобр', 'Животное из отряда грызунов'],
]

print(build_definition_list(definitions))
# <dl><dt>Блямба</dt><dd>Выпуклость, утолщение на поверхности чего-либо</dd><dt>Бобр</dt><dd>Животное из отряда грызунов</dd></dl>

definitions2 = []
print(build_definition_list(definitions2))  # ''

definitions3 = [
    ['HTML', 'HyperText Markup Language'],
]
print(build_definition_list(definitions3))
# <dl><dt>HTML</dt><dd>HyperText Markup Language</dd></dl>