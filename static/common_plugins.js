// canvas background plugin
const backgroundPlugin = {
  id: 'background-plugin',
  beforeDraw: (chart) => {
    const ctx = chart.canvas.getContext('2d');
    ctx.save();
    ctx.globalCompositeOperation = 'destination-over';
    ctx.fillStyle='white';
    ctx.fillRect(0, 0, chart.width, chart.height);
    ctx.restore();
  }
}

// baseLabels plugin block
const baseLabels = {
  id: 'baseLabels',
  afterDatasetsDraw(chart, args, pluginOptions) {
    const { ctx, config, scales: { x, y } } = chart;
    ctx.font = '13px sans-serif';
    ctx.fillStyle = 'gray';

    chart.data.datasets[0].data.forEach((datapoint, index) => {
      const datasetArray = [];
      ctx.textAlign = datapoint.data.effect > 0 ? 'right' : 'left';
      let config_x = config._config.options.scales.x;
      if ('min' in config_x) {
        if (config_x.max < 0) {
          ctx.fillText(datapoint.data.base, x.getPixelForValue(config_x.max), y.getPixelForValue(index)+15);
        } else if (config_x.min > 0) {
          ctx.fillText(datapoint.data.base, x.getPixelForValue(config_x.min), y.getPixelForValue(index)+15);
        } else {
          ctx.fillText(datapoint.data.base, x.getPixelForValue(0), y.getPixelForValue(index)+15);
        }
      } else {
        ctx.fillText(datapoint.data.base, x.getPixelForValue(0), y.getPixelForValue(index)+15);
      }
    })
  }
}

// valueLabels plugin block
const valueLabels = {
  id: 'valueLabels',
  afterDatasetsDraw(chart, args, pluginOptions) {
    const { ctx, config, scales: { x, y } } = chart;
    ctx.font = '13px sans-serif';
    ctx.fillStyle = 'black';

    chart.data.datasets[0].data.forEach((datapoint, index) => {
      ctx.textAlign = datapoint.data.effect > 0 ? 'left' : 'right';
      let config_x = config._config.options.scales.x;
      if ('min' in config_x) {
        console.log(config_x)
        if (datapoint.data.effect - config_x.max > 0) {
          ctx.fillText(datapoint.data.value, x.getPixelForValue(config_x.max), y.getPixelForValue(index)+1);
        } else if (datapoint.data.effect - config_x.min < 0) {
          ctx.fillText(datapoint.data.value, x.getPixelForValue(config_x.min), y.getPixelForValue(index)+1);
        } else {
          ctx.fillText(datapoint.data.value, chart.getDatasetMeta(0).data[index].x + (datapoint.data.effect > 0 ? 5 : -5), y.getPixelForValue(index)+1);
        }
      } else {
        ctx.fillText(datapoint.data.value, chart.getDatasetMeta(0).data[index].x + (datapoint.data.effect > 0 ? 5 : -5), y.getPixelForValue(index)+1);
      }
    })

  }
}
