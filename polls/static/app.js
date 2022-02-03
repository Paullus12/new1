 var vm = new Vue({
  el: '#language',
  data: {
  selected:[ ],
  options: [ ]

  },
  
  created: function() {
    const vm = this;
    axios.get('/api/languages')
    .then(function(response){
    vm.options = response.data

  })

}

}

);

 var vm = new Vue({
  el: '#employment',
  data: {
  selected:[ ],
  options: [ ]

  },
  
  created: function() {
    const vm = this;
    axios.get('/api/employment')
    .then(function(response){
    vm.options = response.data

  })

}

}

);




var vm = new Vue({
  el: '#theme',
  data: {
  selected:[ ],
  options: [ ]

  },
  
  created: function() {
    const vm = this;
    axios.get('/api/theme')
    .then(function(response){
    vm.options = response.data

  })

}

}

);




