<template>
  <div class="q-mt-xs">
    <template v-if="attr.allowCustom">
      <q-input
        :value='value'
        @input='secim'
        dense
        :label="attr.attribute.name"
        :rules="[ val => val && val.length > 0 || 'Lütfen değer belirtin!']"
      />
    </template>
    <template v-else>
      <template v-if="attr.attributeValues.length > 0">
        <q-select
          :value='value'
          @input='secim'
          dense
          outlined
          :label="attr.attribute.name"
          :options="attr.attributeValues"
          option-value="id"
          :option-label="(o) => `${o.name}`"
          :rules="[ val => check(val) ]"
          >
        </q-select>
      </template>
    </template>

  </div>
</template>

<script>
  export default {
    props: {
      value: {
        type: undefined
      },
      attr: {
        type: Object,
        required: true
      }
    },
    methods: {
      check(val){
        if (val ===undefined || val === null) return `Lütfen seçim yapın!`
        return true
      },
      secim (evt) {
        this.$emit('input', evt)
      }
    }
  }
</script>

<style lang="css">
</style>
