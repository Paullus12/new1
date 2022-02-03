console.clear()
Vue.component('select2Multiple', {
  props: ['options', 'value'],
  template: '#select2-template',
  mounted: function () {
    var vm = this
    $(this.$el)
      // init select2
      .select2({ data: this.options })
      .val(this.value)
      .trigger('change')
      // emit event on change.
      .on('change', function () {
        vm.$emit('input', $(this).val())
      })
  },
  watch: {
    value: function (value) {
       if ([...value].sort().join(",") !== [...$(this.$el).val()].sort().join(","))
        $(this.$el).val(value).trigger('change');
    },
    options: function (options) {
      // update options
      $(this.$el).select2({ data: options })
    }
  },
  destroyed: function () {
    $(this.$el).off().select2('destroy')
  }
})

var vm = new Vue({
  el: '#el',
  template: '#demo-template',
  data: {
    selected: [1],
    options: [
      { id: 1, text: 'Hello' },
      { id: 2, text: 'World' },
      { id: 3, text: 'Foo' },
      { id: 4, text: 'Bar' },
      { id: 5, text: 'Baz' },
    ]
  }
});