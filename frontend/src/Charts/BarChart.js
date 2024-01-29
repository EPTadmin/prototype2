import React from "react"
import{Chart as ChartJS, BarElement} from 'chart.js'
import Bar from 'react-chartjs-2'



ChartJS.register(
    BarElement
    )

const BarChart =() => {
    var data = {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
          label: '# of Votes',
          data: [12, 19, 3, 5, 2, 3],
          borderWidth: 1
        }]
      }

    var options = {
        
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }

    return(
        <div>
            <Bar
            data = {data}
            options={options}
            height ={400}
            
            />
        </div>
    )
}

export default BarChart