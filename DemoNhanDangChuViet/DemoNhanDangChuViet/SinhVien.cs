using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DemoNhanDangChuViet
{
    public class SinhVien
    {
        string maso, diemso, diemchu;

        public string Diemchu
        {
            get { return diemchu; }
            set { diemchu = value; }
        }

        public string Diemso
        {
            get { return diemso; }
            set { diemso = value; }
        }

        public string Maso
        {
            get { return maso; }
            set { maso = value; }
        }
        public SinhVien()
        {
        }
        public SinhVien(string maso, string diemso, string diemchu)
        {
            this.maso = maso;
            this.diemso = diemso;
            this.diemchu = diemchu;
        }
    }
}
