<template>
  <div class="row">
    <div class="col-md-12">
      <table class="table">
        <thead>
          <th colspan="7" class="th">Toplam</th>
        </thead>
        <tbody>
          <tr>
            <td v-for="report in data" class="rightTable">
              <span>{{ report.type }}</span>
              <div class="code">
                <span>{{ report.sum }}</span>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  props: {
      days: {
          type: Array,
          default () {
              return []
          }
      },
      data: {
        type: Array,
        default () {
          return []
        }
      }
  }
};
</script>

<style scoped>
table {
  border: 1px solid rgba(240, 149, 149, 0.13);
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
  background-color: #4a4e69;
  color: #e9e9e9;
}

td {
  border: 1px solid rgba(0, 0, 0, 0.13);
  text-align: center;
  padding: 10px 20px;
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

.rightTable {
  background-color: #343a40;
}

.rightTable table {
  border: 0px;
}

.rightTable span {
  color: #edf2f4;
}

.rightTable .code span {
  color: #ffba08;
}
</style>
