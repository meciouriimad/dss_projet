import xml.etree.ElementTree as ET
class DataHandler:
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path
        self.root = self.load_xml_data()

    def load_xml_data(self):
        tree = ET.parse(self.xml_file_path)
        root = tree.getroot()
        return root
    def retreive_all_data(self):
        all_data = []
        for artiste in self.root.findall('artiste'):
            artist_info = {
                'nom': artiste.attrib['nom'],
                'ville': artiste.attrib['ville'],
                'site': artiste.find('site').attrib['url'],
                'biographie': artiste.find('biographie').text
            }
            albums = []
            for album in self.root.findall('album'):
                if album.find('ref-artiste').attrib['ref'] == artiste.attrib['no']:
                    album_info = {
                        'annee': album.attrib['annee'],
                        'reference': album.attrib['reference'],
                        'titre': album.find('titre').text,
                        'chansons': [chanson.text for chanson in album.find('chansons')]
                    }
                    albums.append(album_info)
            artist_info['albums'] = albums
            all_data.append(artist_info)
        return all_data
   
    def retrieve_filtered_data(self, artist_name):
        all_data = self.retreive_all_data()
        filtered_data = []

        for artist in all_data:
            if artist_name.lower() in artist['nom'].lower():
                filtered_data.append(artist)

        return filtered_data

   
    def generate_html(self, all_data):
        # If all_data is a string, convert it to a list containing the string
        if isinstance(all_data, str):
            all_data = [all_data]
       
        html = "<!DOCTYPE html><html><head><title>My Website</title></head><body>"
        html += "<form id='searchForm' action='/filter' method='GET'>"
        html += "<input type='text' placeholder='search' id='search' name='artist_name'>"
        html += "<button type='submit'>Search</button>"
        html += "</form>"
        
        for artist in all_data:
            if isinstance(artist, dict):  # Ensure that artist is a dictionary
                html += "<div class='artist'>"
                html += "<h2>{}</h2>".format(artist['nom'])
                html += "<p>Ville: {}</p>".format(artist['ville'])
                html += "<p>Site: <a href='{}'>{}</a></p>".format(artist['site'], artist['site'])
                html += "<p>Biographie: {}</p>".format(artist['biographie'])
                html += "<h3>Albums</h3>"
                
                for album in artist['albums']:
                    html += "<div class='album'>"
                    html += "<h4>{} ({})</h4>".format(album['titre'], album['annee'])
                    html += "<table border='1'><tr><th>Chanson</th></tr>"
                    
                    for chanson in album['chansons']:
                        html += "<tr><td>{}</td></tr>".format(chanson)
                    
                    html += "</table></div>"
                
                html += "</div>"
        
        html += "</body></html>"
        return html

    def is_similar(self, name1, name2):
        # Compare names case-insensitively
        return name1.lower() == name2.lower()
# datahandelr=DataHandler("./data/artisteDevoir.xml")
# data=datahandelr.retreive_all_data()
# print(data)
# html_content = datahandelr.generate_html()
# print(html_content)


datafilter=DataHandler("./data/artisteDevoir.xml")
data=datafilter.retrieve_filtered_data("FIRGANI mohamed Taher")
# print(data)
content=datafilter.generate_html(data)
print(content)