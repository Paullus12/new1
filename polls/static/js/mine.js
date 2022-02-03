new Vue({
  el: '#student',
  data: {
  students: []

  },
  
  mounted: function() {
    axios.get('/api/students')
    .then(response =>{ this.students = response.data;})
    
    
    

}

}

);




