const app = getApp();
Page({
  data: {
    ColorList: app.globalData.ColorList,
    shows: false
  },
  SetShadow(e) {
    this.setData({
      shadow: e.detail.value
    })
  },
  SetBorderSize(e) {
    this.setData({
      bordersize: e.detail.value
    })
  }
})
