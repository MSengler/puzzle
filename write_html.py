import numpy as np




def generate(nb_row = 2, nb_col = 4, width=1024, height=512):

	k = min(1024/width, 1024/height)
	width *= k
	height *= k 

	begin = """
	<!DOCTYPE HTML>
	<html>
	<head>

	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" type="text/css">
	<title>puzzle</title>
	"""

	style = f"""
	<style>
		.grid-cell {{
			width: {int(width/nb_col)}px;
			height: {int(height/nb_row)}px;
			border: 1px solid #aaaaaa;
			position: relative;
		}}

		.carte {{
			margin-top: 10px;
			float:left;	
			padding : 15px 10px 15px 25px; 
			width: {width+10}px; 	
			height : {height+10}px; 
			background : whitesmoke; 
		}}

		.morceaux {{	
			margin-top: 10px;
			margin-left : {width+50}px; 		
			padding : 15px 10px 15px 10px; 	
			width: {min(width,height) + 10}px; 	
			height : auto; 
			background-color : #2f5ec4; 
			font-size: x-large;
		}}

	</style>
	"""

	script = """
	<script>
		function allowDrop(ev) {
		ev.preventDefault();
		}

		function drag(ev) {
		ev.dataTransfer.setData("text", ev.target.id);
		}

		function drop(ev) {
		ev.preventDefault();
		var data = ev.dataTransfer.getData("text");

		if (ev.target.classList.contains('grid-cell') && ev.target.children.length === 0) {
			ev.target.appendChild(document.getElementById(data));
		} 
		}
	</script>
	</head>
	"""

	nav = """
	<body>
		<header>Puzzle du monde </header>

		    <nav class="menu">
        <ul class="menu-list">
            <li class="menu-item">
                <a href="/">Accueil</a>
            </li>
            <li class="menu-item">
                <a href="#">Monde</a>
                <ul class="submenu">
                    <li><a href="/run-monde_f">Facile</a></li>
                    <li><a href="/run-monde_m">Moyen</a></li>
                    <li><a href="/run-monde_d">Difficile</a></li>
                </ul>
            </li>
			<li class="menu-item">
                <a href="#">Asie</a>
                <ul class="submenu">
                    <li><a href="/run-asie_f">Facile</a></li>
                    <li><a href="/run-asie_m">Moyen</a></li>
                    <li><a href="/run-asie_d">Difficile</a></li>
                </ul>
            </li>
            <li class="menu-item">
                <a href="#">Importer</a>
            </li>
            <li class="menu-item">
                <a href="#">À propos</a>
            </li>
        </ul>
    </nav>
	"""

	map_cell = """
		<div class="carte">
			<table border="0" cellspacing="0" cellpadding="0">
	"""

	idx_id = 0
	for i in range(nb_row):
		map_cell = map_cell + "        <tr>\n"
		for j in range(nb_col):
			map_cell = map_cell + f"""            <td><div id="cell{idx_id}" class="grid-cell" ondrop="drop(event)" ondragover="allowDrop(event)"></div></td>\n"""
			idx_id += 1
		map_cell = map_cell + "        </tr>\n"

	map_cell = map_cell + "        </table>\n    </div>\n"


	morceaux = """
		<div class="morceaux">
			Placer les morceaux sur la carte:
			<table border="0" cellspacing="0" cellpadding="0">
	"""

	index = np.stack([np.repeat(range(nb_row),nb_col),np.array(list(range(nb_col))*nb_row) ], axis=1)
	index = np.random.permutation(index)

	idx = 0
	max_cr = max(nb_col,nb_row)
	min_cr = min(nb_col,nb_row)
	for i in range(max_cr):
		morceaux = morceaux + "        <tr>\n"
		for j in range(min_cr):
			morceaux = morceaux + f"""            <td colspan="3"><img id="drag{idx}" src="{{{{ url_for('static', filename='images/piece_{index[idx,0]}_{index[idx,1]}.png') }}}}" draggable="true" ondragstart="drag(event)" width="{int(width/nb_col)}" height="{int(height/nb_row)}"></td>\n"""
			idx += 1
		morceaux = morceaux + "        </tr>\n"

	morceaux = morceaux + """
			</table>
		</div>	

	</body>
	</html>
	"""

	with open(f"templates/puzzles.html", 'w') as f:
		f.write(begin)
		f.write(style)
		f.write(script)
		f.write(nav)
		f.write(map_cell)
		f.write(morceaux)
