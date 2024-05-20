<template>

    <div v-if="Object.keys(cell).length > 0">
      <span class="day">{{ cell.tr_day }}</span>
      <div class="code">
        <template v-if="cell.waiting == true">
          <span class="newly">{{
            `${cell.excuse} (${
              cell.excuse_day == 0 ? "TG" : cell.excuse_day == 1 ? "ÖÖ" : "ÖS"
            })`
          }}</span>
        </template>

        <template v-else>
          <span>{{
            `${cell.excuse} (${
              cell.excuse_day == 0 ? "TG" : cell.excuse_day == 1 ? "ÖÖ" : "ÖS"
            })`
          }}</span>
        </template>
      </div>
    </div>
    <div v-else class="no-data">
        <span></span>
        <div>
          <span></span>
        </div>
    </div>
  
</template>

<script>
export default {
  props: {
    cell: {
      type: Object,
      default: null
    }
  }
};
</script>

<style scoped>
table {
  border: 1px solid rgba(0, 0, 0, 0.13);
  border-collapse: collapse;
  width: 100%;
}

th {
  border: 1px solid rgba(0, 0, 0, 0.13);
  text-align: center;
  padding: 10px 0;
  width: 150px;
}

table thead th {
  background-color: #22223b;
  color: #221c35;
  margin: 10px 20px;
}

.day {
  color: rgba(40, 48, 62, 0.6);
  font-weight: normal;
  position: absolute;
  top: 15px;
  left: 15px;
}

div > span {
  color: #309975;
  font-weight: bold;
}

.no-data {
  height: 100%;
  width: 100%;
  background: repeating-linear-gradient(
    45deg,
    #bdbdbf93,
    #bdbdbf93 10px,
    #acacac80 10px,
    #acacac80 20px
  );
}

.newly {
  color: #dc986b;
}
</style>
