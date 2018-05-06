using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DemoNhanDangChuViet
{
    public partial class fShowImage : Form
    {
       // string path = "D:\\nhandienchuviet\\KL_Project\\DemoNhanDangChuViet\\DemoNhanDangChuViet\\Python_Master\\bangdiem1.PNG";
        public fShowImage(string path)
        {
            InitializeComponent();
            showImageInput(path);
        }
        public void showImageInput(string path)
        {
//            Bitmap bmp = new Bitmap(@"D:\KhoaLuan\KL_Project\DemoNhanDangChuViet\DemoNhanDangChuViet\Python_Master\bangdiem_contours.png");
            Bitmap bmp = new Bitmap(@""+path+"");
            pictureBox1.Image = bmp;
        }
        public void setPath(string path) {
         ///   this.path = path;
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void fShowImage_Load(object sender, EventArgs e)
        {

        }

    }
}
