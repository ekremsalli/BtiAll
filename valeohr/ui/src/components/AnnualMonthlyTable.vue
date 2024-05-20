<template>
  <div class="row table-div">
    <div class="col-md-12">
      <span class="text-h4 month-title" v-if="name">{{ c_name }}</span>
      <q-btn
        style="min-height: 35px"
        outline
        color="primary"
        @click="$emit('show_panel')"
        class="on-right q-mb-md"
        label="Yeni Kayıt Ekle"
      />
      <table class="table">
        <thead>
          <th v-for="day in days" class="th">{{ day }}</th>
        </thead>
        <tbody>
          <tr v-for="row in 5">
            <td v-for="col in 7">
              <template v-if="specific_day(row, col).length > 0" >
                <display-annual-cell
                  v-for="(cell, key) in specific_day(row, col)"
                  :key="key"
                  :cell="cell"
                ></display-annual-cell>
              </template>
              <template v-else>
                <display-annual-cell
                  :cell="{}"
                ></display-annual-cell>
              </template>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { date } from "quasar";
import DisplayAnnualCell from "./DisplayAnnualCell";

export default {
  components: {
    DisplayAnnualCell
  },
  data() {
    return {
      style_color: false
    };
  },
  props: {
    days: {
      type: Array,
      default() {
        return [];
      }
    },
    data: {
      type: Array,
      default() {
        return [];
      }
    },
    name: {
      type: Object,
      required: true
    }
  },
  computed: {
    c_name() {
      return date.formatDate(
        date.buildDate({
          year: this.name.year,
          date: 1,
          month: this.name.month
        }),
        "MMMM - YYYY"
      );
    }
  },
  methods: {
    specific_day(week, day) {
      let self = this;
      let data = this.data.filter(o => o.week == week && o.day == day - 1);
      if (data) {
        return data;
      }
      return [];
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
  color: #f2e9e4;
}

td {
  border: 1px solid rgba(0, 0, 0, 0.13);
  text-align: center;
  /* padding: 10px 20px; */
  font-style: normal;
  font-size: 22px;
  line-height: 26px;
  color: rgba(0, 0, 0, 0.5);
  height: 125px;
}

table tbody td {
  background-color: #fefefe;
  position: relative;
}

table tbody td > span {
  color: rgba(125, 121, 121, 0.63);
  font-weight: bold;
  position: absolute;
  top: 15px;
  left: 15px;
}

table tbody td > div > span {
  color: rosybrown;
}

.filterRow {
  background: #fff;
  padding: 10px 0;
}

.table-div {
  margin-top: 20px;
}

.month-title {
  margin-top: 10px;
}
</style>
