
from gexf import Gexf
from lxml import etree
from model.chanye_zhuanye import search_xueke,search_chanye,search_chanye_zhuan,search_chanye_id


import faker
f = faker.Faker(locale='zh-CN')

chanye = search_chanye()
zhuanye = search_xueke()
chanye_zhuanye = search_chanye_zhuan()
chanye_id = search_chanye_id()

print(type(chanye_zhuanye.keys()))

gexf = Gexf("chanye","zhuanye")
graph = gexf.addGraph("chanye","jiaoyu","zhuanye")

atr1 = graph.addNodeAttribute(force_id='modularity_class',title = 'chanye',defaultValue='true',type='integer')
atr2 = graph.addNodeAttribute(force_id='zhuanye',title='zhuan_ye',defaultValue='true',type='string')



for node in chanye:
    node_type = 'chanye'
    tmp_node = graph.addNode(str(node[0]), str(node[1]))
    tmp_node.addAttribute(atr1,str(int(node[0])-1))
for node in zhuanye:
    node_type = 'zhuanye'
    tmp_node = graph.addNode(str(node[0]), str(node[1]))
    tmp_node.addAttribute(atr2, node_type)


j = 0
for node in chanye_zhuanye:
    for i in chanye_zhuanye[node]:
        graph.addEdge(str(j),str(node),str(i),weight=str(len(chanye_zhuanye[node])))
        j+=1

node_id_list = []
for i in chanye:
    node_id_list.append(str(i[0]))
for j in zhuanye:
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
                    if tmp_id in chanye_id and tmp_id in chanye_zhuanye.keys():
                        node_id = tmp_id
                        node_rgb = node_rgb_list[node_id]
                        size_value = str(len(chanye_zhuanye[node_id])*5)
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
