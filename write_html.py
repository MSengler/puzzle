import numpy as np




def generate(nb_row = 2, nb_col = 4, width=1024, height=512):

	#k = min(1024/width, 1024/height)
	k = min(45/width, 45/height)
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
			width: {int(width/nb_col)}vw;
			height: {int(height/nb_row)}vw;
			border: 1px solid #aaaaaa;
			position: relative;
		}}

		.carte {{
			margin-top: 10px;
			float:left;	
			padding : 15px 10px 15px 25px; 
			width: {width+1}vw; 	
			height : {height+1}vw; 
			background : whitesmoke; 
		}}

		.morceaux {{	
			margin-top: 10px;
			margin-left : {width+10}vw; 		
			padding : 15px 10px 15px 10px; 	
			width: {min(width,height) + 1}vw; 	
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
			const pieceId = ev.dataTransfer.getData("text");
			const caseId = ev.target.id;
			//console.log(caseId);

			// Vérifier si la case est vide et placer le morceau
			if (ev.target.classList.contains('grid-cell') && ev.target.children.length === 0) {
				ev.target.appendChild(document.getElementById(pieceId));
			} 
			// Vérifier si le morceau est bien placé
			if (pieceId.replace("drag", "") === caseId.replace("cell", "")) {
				console.log("Bien placé :", pieceId, caseId);
				checkCompletion()
			} else {
				console.log("Mauvaise position :", pieceId, caseId);
			}

			
		}

		function checkCompletion() {
			const dropzones = document.querySelectorAll('.grid-cell');
			let correct = 0;
			dropzones.forEach(zone => {
				if (zone.children.length > 0) {
				const piece = zone.children[0];
				//console.log(piece.id, zone.id);
				const pieceCoords = piece.id.replace(/^drag_/, '');
				const zoneCoords  = zone.id.replace(/^cell_/, '');
				if (pieceCoords === zoneCoords) {correct++;}

			}
			});

			if (correct === dropzones.length) {
				alert('🎉 Puzzle complété !');
			} else {
				console.log(`Progression: ${correct} / ${dropzones.length}`);
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
                <button id="uploadBtn">Importer</button>
                <form id="uploadForm" action="/upload" method="POST" enctype="multipart/form-data" style="display: none;">
                    <input type="file" name="file" id="fileInput" accept="image/*">
                </form>
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

	for i in range(nb_row):
		map_cell = map_cell + "        <tr>\n"
		for j in range(nb_col):
			map_cell = map_cell + f"""            <td><div id="cell_{i}_{j}" class="grid-cell" ondrop="drop(event)" ondragover="allowDrop(event)"></div></td>\n"""
		map_cell = map_cell + "        </tr>\n"

	map_cell = map_cell + "        </table>\n    </div>\n"


	morceaux = """
		<div class="morceaux">
			Placer les morceaux sur la carte:
			<table border="0" cellspacing="0" cellpadding="0">
	"""

	index = np.stack([np.repeat(range(nb_row),nb_col),np.array(list(range(nb_col))*nb_row) ], axis=1)
	index = np.random.permutation(index)


	max_cr = max(nb_col,nb_row)
	min_cr = min(nb_col,nb_row)
	idx = 0
	for i in range(max_cr):
		morceaux = morceaux + "        <tr>\n"
		for j in range(min_cr):
			morceaux += f"""
			<td colspan="3">
        		<img id="drag_{index[idx,0]}_{index[idx,1]}" 
             		src="{{{{ url_for('static', filename='images/piece_{index[idx,0]}_{index[idx,1]}.png') }}}}" 
             		draggable="true" 
             		ondragstart="drag(event)"
             		style="width: {int(width / nb_col)}vw; height: {int(height / nb_row)}vw;">
    		</td>\n"""
			idx += 1
			if idx >= nb_col * nb_row:
				break
		morceaux = morceaux + "        </tr>\n"

	morceaux = morceaux + """
			</table>
		</div>	
	"""

	script2="""
	<script>
		document.getElementById("uploadBtn").addEventListener("click", function() {
        	document.getElementById("fileInput").click(); // Simule le clic sur l'input
        });
        
        document.getElementById("fileInput").addEventListener("change", function() {
        	document.getElementById("uploadForm").submit(); // Soumet le formulaire dès qu'un fichier est sélectionné
        });
	</script>
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
		f.write(script2)
