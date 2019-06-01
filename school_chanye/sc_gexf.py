
from gexf import Gexf
from lxml import etree
from model.school_chanye import search_school,search_chanye,search_school_chanye,search_school_id

import faker
f = faker.Faker(locale='zh-CN')


school = search_school()
chanye = search_chanye()
school_chanye = search_school_chanye()
school_id = search_school_id()

gexf = Gexf("school","chanye")
graph = gexf.addGraph("school","jiaoyu","chanye")

atr1 = graph.addNodeAttribute(force_id='modularity_class',title = 'schoolce',defaultValue='true',type='integer')
atr2 = graph.addNodeAttribute(force_id='chanye',title='chan_ye',defaultValue='true',type='string')

for node in school:
    node_type = 'school'
    tmp_node = graph.addNode(str(node[0]),str(node[1]))
    tmp_node.addAttribute(atr1,str(node[0]-1))


for node in chanye:
    node_type = 'chanye'
    tmp_node = graph.addNode(str(node[0]), str(node[1]))
    tmp_node.addAttribute(atr2, node_type)


j = 0
for node in school_chanye:
    for i in school_chanye[node]:
        graph.addEdge(str(j),str(node),str(i),weight=len(school_chanye[node]))
        j+=1


node_id_list = []
for i in school:
    node_id_list.append(str(i[0]))
for j in chanye:
    node_id_list.append(str(j[0]))
node_rgb_list = {}
import random
for i in node_id_list:
    node_rgb_list.setdefault(i, []).append(f.rgb_color())


output_file=open('data.gexf', "wb")

gexf_xml = gexf.getXML()

for gexf_elem in gexf_xml:
    if gexf_elem.tag == 'graph':
        for gexf_nodes_links in gexf_elem:
            if gexf_nodes_links.tag == 'nodes':
                print("dealing with nodes viz")
                for node in gexf_nodes_links:
                    tmp_id = node.get('id')
                    # print(tmp_id)
                    if tmp_id in school_id and int(tmp_id) in school_chanye.keys():
                        node_id = tmp_id
                        node_rgb = node_rgb_list[node_id]
                        # size_value = str(len(school_xuke[node_id]))
                        print(str(len(school_chanye[int(node_id)])))
                        size_value = str(len(school_chanye[int(node_id)]))
                        size = etree.SubElement(node, '{%s}size' % gexf.viz)
                        size.set('value', size_value)
                    else:
                        node_id = tmp_id
                        node_rgb = node_rgb_list[node_id]
                        # size_value = str(len(school_xuke[node_id]))
                        size_value = str(4)
                        size = etree.SubElement(node, '{%s}size' % gexf.viz)
                        size.set('value', size_value)
                    position = etree.SubElement(node, '{%s}position' % gexf.viz)
                    position.set('x',str(random.uniform(-900,900)))
                    position.set('y', str(random.uniform(-900,900)))

                    color = etree.SubElement(node, '{%s}color' % gexf.viz)
                    node_rgb = node_rgb[0]
                    node_rgb = node_rgb.split(',')
                    color.set('r', node_rgb[0])
                    color.set('g', node_rgb[1])
                    color.set('b', node_rgb[2])

output_file.write(etree.tostring(gexf_xml, pretty_print=True, encoding='utf-8', xml_declaration=True))
output_file.close()
