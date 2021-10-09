# วิธีติดตั้ง

Clone repository ไปลงในเครื่องตัวเองก่อน (พิมพ์ใน terminal หรือ command prompt ต้องลง git ก่อนนะ) 
```
git clone https://github.com/LittleLunar/OrangeClassificationDeepLearning.git
```
หลังจาก clone เสร็จ ทำการแยก Branch ด้วยคำสั่ง
> git branch {ชื่อ Branch} เช่น
```
git branch o-training
```

หลังจากสร้าง Branch ให้ทำการย้ายไปที่ Branch ทีเราสร้างด้วยคำสั่ง
> git checkout {ชื่อ Branch} เช่น
```
git checkout o-training
```
หลังจากที่ย้าย Branch แล้วพิมพ์คำสั่งนี้เพือเช็คอีกทีว่าอยู่ถูก Branch
```
git branch 
```
- ถ้าทำถูกต้องจะต้องมี * อยู่หน้า Branch ที่เราย้ายมา
![image](https://user-images.githubusercontent.com/50941709/136656798-3ca450b4-3d3d-417f-a920-4e08768366be.png)

ทำ virtualenv ด้วยคำสั่ง (สำหรับวิธีการทำ virtualenv : https://www.youtube.com/watch?v=APOPm01BVrk)
```
virtualenv venv
```

หลังจากนั้นจะต้องมีโฟลเดอร์ venv เพิ่มขึ้นมา
---
![image](https://user-images.githubusercontent.com/50941709/136656885-b2916768-b1ca-48b4-bfdc-57fd399f9185.png)

หลังจากมีไฟล์ venv ให้พิมพ์คำสั่งตามนี้ (ถ้าทำใน window powershell)
```
.\venv\Scripts\activate
```
ถ้าทำถูกจะขึ้นแบบนี้ (env) ขึ้นมา
---
![image](https://user-images.githubusercontent.com/50941709/136656970-5cd84517-dcb9-4237-ba66-f5ef365b84eb.png)


ทำการ pip install libraries ที่ใช้ในโปรเจค (ใช้ python 3.9.7 ขึ้นไปนะ)
```
pip install -r requirements.txt
```

ถ้าไม่ error ก็ไปขั้นตอนถัดไปคือ เปิด ide ขึ้นมา (ใช้ vscode ถ้าไม่มีก็ไปลงนะ ถ้าจะใช้วิธีนี้)
```
code .
```

หลังจากเปิด vscode ให้ลง extension สำหรับ jupyter (โอใช้ตัวนี้ไม่มีปัญหาอะไร)
![image](https://user-images.githubusercontent.com/50941709/136657104-777a8aeb-bd78-4d4b-9822-e9d807f2a088.png)

ทำการเปิดไฟล์ main.ipynb แล้วกดตรงมุมขวาบนเพื่อเลือก kernel
![image](https://user-images.githubusercontent.com/50941709/136657136-b0775ab0-1e89-4e6d-8c80-12507232ee36.png)

เลือกอันนี้
![image](https://user-images.githubusercontent.com/50941709/136657157-b56ede9e-078c-4d49-80f1-00517a026376.png)

---

### ขั้นตอนถัดไปก็ปรับโค้ดให้คุณภาพมันดีขึ้นใน Accuracy สูง และ Loss function ต่ำ

---

หลังจากที่รันโค้ดแล้วได้ Accuracy สูง และ Loss function ต่ำ ให้แคปภาพลงในโฟลเดอร์ Model/{โฟลเดอร์ Model ที่เรากำหนดในโค้ด} 
![image](https://user-images.githubusercontent.com/50941709/136657230-f8264f6f-0337-433e-9d11-986eb0991975.png)

รันคำสั่งนี้เพื่อลบภาพที่ถูก Augmentation
```
python delAug.py หรือ py delAug.py
```

อัพโค้ดขึ้น github

```
git add .
```

```
git status
```
> เช็คว่าไฟล์ที่ถูก add เข้ามามีอะไรบ้าง ถ้ามันขึ้นแบบเยอะมากๆๆๆๆๆๆๆๆๆ แสดงว่า .gitignore มีปัญหา ให้บอกในกลุ่ม

```
git commit -m "{ชื่อของการ commit ครั้งนั้น}"
```

### สำคัญขั้นตอนนี้ git push origin {ชื่อ branch ตัวเอง} เท่านั้น **ห้ามพิมพ์ git push origin main เด็ดขาด**
เช่น
```
git push origin o-training (สำหรับ branch โอ คนอื่นก็พิมพ์เป็นชื่อ branch ตัวเอง)
```
- **โค้ดจะถูกส่งขึ้นไปบน github**

## สุดท้าย

> **ถ้าได้ผลลัพธ์ที่ดีสามารถทำขอ Pull request กับ Branch main ได้ (ห้าม Merge ตรงๆ เด็ดขาด)**

--- 
