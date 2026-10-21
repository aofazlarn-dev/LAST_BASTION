import numpy as np, os, json
from PIL import Image
from scipy import ndimage
import sys; SRC=sys.argv[1] if len(sys.argv)>1 else 'assets/sheets'; OUT=sys.argv[2] if len(sys.argv)>2 else 'build/cut'; os.makedirs(OUT, exist_ok=True)
V=['0','1','2','3','4']
def fam(cols, rows): return [[f'{c}{r}' for c in cols] for r in rows]
SHEETS={
 'core_units_buildings.png':(5,4,[['hero_archer','hero_warrior','hero_mage','hero_engineer','hero_healer'],['worker','worker_wood','worker_stone','u_archer','u_sword'],['u_medic','camp1','camp2','camp3','camp4'],['camp5','wall1','wall2','wall3','gate1']]),
 'buildings_tiles_items.png':(5,4,[['gate2','gate3','tower1','tower2','tower3'],['barracks','infirmary','workshop','grass','tree1'],['tree2','rock',  'stump','pebbles','water'],['bow_common','bow_rare','bow_epic','armor_common','armor_rare']]),
 'items_fx.png':(5,2,[['armor_epic','fx_arrow','fx_bolt','fx_blast','fx_heal'],['x_amulet','x_gauntlet','x_crystal','fx_flame','fx_frost']]),
 'monsters_low.png':(5,5,fam(['zombie','wolf','slime','bat','skel'],V)),
 'monsters_mid_a.png':(5,4,fam(['ghoul','spider','orc','wisp','bonemage'],V[:4])),
 'monsters_mid_b.png':(5,4,[['ghoul4','spider4','orc4','wisp4','bonemage4'],['ghoul7','spider7','orc7','wisp7','bonemage7'],['ghoul6x','spider6x','orc6x','wisp6x','bonemage6x'],['ghoul2x','spider2x','orc2x','wisp2x','bonemage2x']]),
 'monsters_high_a.png':(5,4,fam(['knight','were','golem','demon','lich'],V[:4])),
 'monsters_high_b.png':(5,4,[['knight4','were4','golem4','demon4','lich4'],['knight7','were7','golem7','demon7','lich7'],['knight6x','were6x','golem6x','demon6x','lich6x'],['knight2x','were2x','golem2x','demon2x','lich2x']]),
 'monsters_bosses.png':(5,1,[['boss0','boss1','boss2','boss3','boss4']]),
}
SHEETS.update({
 'items_18.png':(4,5,[['bow_common1','bow_common2','bow_common3','x_e1'],['bow_rare1','bow_rare2','bow_rare3','x_e2'],['bow_epic1','bow_epic2','bow_epic3','x_e3'],['armor_common1','armor_common2','armor_common3','armor_rare3'],['armor_epic1','armor_rare2','armor_epic2','armor_epic3']]),
 'environment_fx.png':(4,4,[['ground_forest','ground_rocky','ground_waste','tuft'],['flower','firepit','loot_bag','fx_fireball'],['fx_sunburn','fx_hit','fx_recall','fx_rubble'],['fx_levelup','fx_volley','fx_web','fx_frostbolt']]),
 'ui_icons.png':(6,5,[['ui_army','ui_bag','ui_bestiary','ui_build','ui_day','ui_exp'],['ui_home','ui_hp','ui_map','ui_menu','ui_night','ui_repair'],['ui_res_heroweapon','ui_res_unitarmor','ui_res_unitweapon','ui_mode_guard','ui_mode_free','ui_mode_follow'],['ui_mp','ui_stone','ui_warn','ui_wood','ui_worker','ui_skill_volley'],['x_u1','x_u2','x_u3','x_u4','x_u5','x_u6']]),
})
TILE={'grass','water','ground_forest','ground_rocky','ground_waste'}
meta={}
for f,(C,R,names) in SHEETS.items():
    im=np.array(Image.open(os.path.join(SRC,f)).convert('RGBA')).astype(np.uint8)
    H,W=im.shape[:2]; cw,ch=W/C,H/R
    mask=im[...,3]>40; lab,num=ndimage.label(mask)
    sizes=ndimage.sum(mask,lab,range(1,num+1)); com=ndimage.center_of_mass(mask,lab,range(1,num+1))
    cid=np.full(num+1,-1)
    for i,(sz,(cy,cx)) in enumerate(zip(sizes,com)):
        if sz<150: continue
        cid[i+1]=min(R-1,int(cy//ch))*C+min(C-1,int(cx//cw))
    own=cid[lab]; own[lab==0]=-1
    objs=ndimage.find_objects(lab)
    yy,xx=np.mgrid[0:H,0:W]; gridc=np.minimum(R-1,(yy//ch).astype(int))*C+np.minimum(C-1,(xx//cw).astype(int))
    for i,sl in enumerate(objs):
        if sl is None: continue
        if (sl[0].stop-sl[0].start)>1.25*ch or (sl[1].stop-sl[1].start)>1.7*cw:
            m=lab==(i+1); own[m]=gridc[m]   # ภาพติดกัน: แบ่งตามช่อง
    other_of=lambda k: (own>=0)&(own!=k)
    for r in range(R):
        for c in range(C):
            n=names[r][c]
            x0,y0,x1,y1=int(c*cw),int(r*ch),int((c+1)*cw),int((r+1)*ch)
            # ขยายกรอบเล็กน้อยเผื่อภาพล้นช่อง แล้วตัดส่วนของช่องข้าง ๆ ออกด้วย component
            px,py=int(cw*0.08),int(ch*0.08)
            X0,Y0,X1,Y1=max(0,x0-px),max(0,y0-py),min(W,x1+px),min(H,y1+py)
            cell=im[Y0:Y1,X0:X1].copy()
            if n.startswith('x_'): continue
            if n in TILE:
                # พื้นผิว: ตัดเฉพาะสี่เหลี่ยมทึบ
                m=cell[...,3]>200; lab,num=ndimage.label(m); sz=ndimage.sum(m,lab,range(1,num+1)); m=lab==(int(np.argmax(sz))+1); ys,xs=np.where(m)
                sub=cell[ys.min():ys.max()+1, xs.min():xs.max()+1]
                k=6; sub=sub[k:-k,k:-k]
                Image.fromarray(sub).save(f'{OUT}/{n}.png'); meta[n]=sub.shape[:2]; continue
            sel=(own==(r*C+c))
            if n.startswith('x_'): continue
            if not sel.any(): print('EMPTY',n); continue
            near=ndimage.binary_dilation(sel,iterations=12) & ~ndimage.binary_dilation(other_of(r*C+c),iterations=3)
            ys,xs=np.where(near); 
            cell=im.copy(); cell[~near]=0; cell[cell[...,3]<10]=0
            ys,xs=np.where(cell[...,3]>0)
            if f=='items_18.png' and r>=3:
                ya,yb=(585,782) if r==3 else (782,1024)
                cell=im.copy(); m2=np.zeros(cell.shape[:2],bool); m2[ya:yb,x0:x1]=True; cell[~m2]=0; cell[cell[...,3]<10]=0
            if n.startswith('bow_') or n.startswith('armor_'):
                mk=cell[...,3]>60; lb,nn=ndimage.label(mk)
                if nn>1:
                    sz=ndimage.sum(mk,lb,range(1,nn+1)); keep=lb==(int(np.argmax(sz))+1)
                    keep=ndimage.binary_dilation(keep,iterations=10); cell[~keep]=0
                ys,xs=np.where(cell[...,3]>0)
            sub=cell[ys.min():ys.max()+1, xs.min():xs.max()+1]
            Image.fromarray(sub).save(f'{OUT}/{n}.png'); meta[n]=sub.shape[:2]
json.dump(meta,open(os.path.join(OUT,'meta.json'),'w'),indent=0)
print(len(meta))
