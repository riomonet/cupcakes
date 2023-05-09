
async function get_list() {

    res = await axios.get("http://127.0.0.1:5000/api/cupcakes")
    return res
    
    
}

async function render_list() {

    cupcake_list = await get_list();
    t = cupcake_list.data.cupcakes
    for (cupcake of t)
	$('#cupcake_list')
	.append (`<tr>
	<td> ${cupcake.flavor} </td>
	<td> ${cupcake.size}   </td>
	<td> ${cupcake.rating} </td>
	</tr>`)
}


render_list()


$('#add-cupcake').on('submit', async function(evt) {

    evt.preventDefault()

    flavor = $('#flavor').val()
    size = $('#size').val()
    rating = $('#rating').val()
    url = $('#url').val()
    console.log(flavor,size,rating,url)

    cupcake = {"flavor": flavor, "size" : size, "rating" : rating}

    res = await axios.post("http://127.0.0.1:5000/api/cupcakes",cupcake)

    clear_table()
    clear_form()
    render_list()
    
})

function clear_table() {
    $('#cupcake_list').empty()
}

function clear_form() {
    $('#add-cupcake :input').val('')
}












