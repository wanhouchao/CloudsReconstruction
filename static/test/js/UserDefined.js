var cun=1;
function Add(element) {
	// 新增一行
	var tr = ('<tr id="code_'+cun+'"><td><select name="action" class="form-control" id="action_'+cun+'"><option>Click</option><option>Clear</option><option>Write</option><option>Switch_to</option><option>Default_content</option><option>Text_up</option><option>Switch_to_window</option><option>Close_win</option><option>FindElement</option></select></td><td><input name="elements" type="text" id="action_0" class="form-control" placeholder="Please enter element" style="width:600px;" /></td><td><button type="button" class="btn btn-primary" id="add_'+cun+'" onclick="Add(this)">新增</button></td><td><button type="button" class="btn btn-primary" id="delete_'+cun+'" onclick="Delente(this)">删除</button></td></tr>');
	$('#table_codeList').append(tr);
	cun++;
	}
	
function Delente(element){
	var num = element.id.split("_")[1];
	if(num!='0'){
		element.parentNode.parentNode.remove(element.parentNode);
	}else{
		alert('兄弟不要瞎玩，第一行怎么能删除！')
	}
	
	// alert(num);
	
}

