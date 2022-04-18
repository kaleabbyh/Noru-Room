var updateBtns = document.getElementsByClassName('update-book')

for (i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var bedId = this.dataset.bed
		var action = this.dataset.action
// user is global obtained in header.html
		console.log('bedId:', bedId, 'Action:', action)
        if (user == 'AnonymousUser'){
			console.log('User is not authenticated')
			
		}else{
			updateUserOrder(bedId, action)
		}

	})
}




function updateUserOrder(bedId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'bedId':bedId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    console.log("data:",data)
            location.reload()
		});
}